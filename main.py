import logging
import sys
import os

from skills.utils import SkillManager
from game import create_env, get_achievements
from agents.sdk import sdk
from agents.action_agent import ActionAgent
from agents.critic_agent import CriticAgent
from agents.curriculum_agent import CurriculumAgent
from primitives.wrapper import SaveStateWrapper
from craftax.craftax_env import make_craftax_env_from_name
import os
import importlib.util
import sys

def import_all_modules_from_folder(folder_path):
    modules = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            module_name = filename[:-3]  # Remove the .py extension
            module_path = os.path.join(folder_path, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            modules[module_name] = module
    return modules

def create_eval_context(modules):
    eval_context = {}
    for module_name, module in modules.items():
        for attr_name in dir(module):
            if not attr_name.startswith('__'):
                eval_context[attr_name] = getattr(module, attr_name)
    return eval_context

modules = import_all_modules_from_folder("primitives")

eval_context = create_eval_context(modules)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)

SEED = 0xBAD_5EED_B00B5


def invoke_action(state, code):
    global eval_context
    code = "from primitives import * \n" + code
    code = "\treturn env"
    
    try:
        func = eval(f"from path import func_name")
        func(state)
        return "No errors"
    except Exception as e:
        return f"thrown exception: {str(e)}"


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger("main_logger")
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)

    with open(log_dir + "/actions.txt", "w") as f:
        pass

    logger.info("Started")

    skill_manager = SkillManager("./skills/chroma_db", sdk)
    curriculum_agent = CurriculumAgent()
    action_agent = ActionAgent()
    critic_agent = CriticAgent()

    env = SaveStateWrapper(make_craftax_env_from_name("Craftax-Symbolic-v1", auto_reset=False), SEED, "logs/action.csv")
    obs, state = env.reset()

    game_finished = False
    while not game_finished:
        exploration_progress = curriculum_agent.get_exploration_progress(state)
        final_task = curriculum_agent.propose_next_task(
            state, exploration_progress
        )
        subtasks = curriculum_agent.task_decomposition(state, final_task)
        for task in subtasks:
            code = None
            # environment_feedback = None
            execution_errors = None
            critique = None
            success = False
            prev_state = env.saved_state
            skills = skill_manager.fetch_skills(task)
            for i in range(4):
                state = prev_state

                code = action_agent.generate_code(code, execution_errors, state, task, skills, critique)
                execution_errors = invoke_action(state, code)
                success, critique = critic_agent.check_task_success(
                    state, task, skills
                )
                if success:
                    logger.info(f"{task} passed!")
                    break
                else:
                    logger.info(f"{task} not passed!")
                directory = os.path.join('./logs', task)
                path = os.path.join(f'./logs/{task}', f"{i}.py")
                os.makedirs(directory, exist_ok=True)
                with open(path, "w", encoding="utf-8") as file:
                    file.write(code)
                    file.write(execution_errors)
            if success:
                skill_manager.add_skill(code)
                curriculum_agent.add_completed_task(task)
            else:
                curriculum_agent.add_failed_task(task)

    logger.info(get_achievements(state))
    logger.info("Finished")
