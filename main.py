import logging
import sys
import os

from skills.utils import SkillManager
from game import create_env, get_achievements
from agents.sdk import sdk
from agents.curriculum_agent import CurriculumAgent
from primitives.wrapper import SaveStateWrapper

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)

SEED = 0xBAD_5EED_B00B5


def invoke_action(state, code):
    try:
        func = eval(code)
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
    action_agent = ...
    critic_agent = ...

    env = SaveStateWrapper(create_env(SEED), SEED, "logs/action.csv")
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

                code = action_agent.generate_code(
                    task, code, execution_errors, critique, skills
                )
                execution_errors = invoke_action(state, code)
                success, critique = critic_agent.check_task_success(
                    task, state
                )
                if success:
                    break
            if success:
                skill_manager.add_skill(code)
                curriculum_agent.add_completed_task(task)
            else:
                curriculum_agent.add_failed_task(task)

    logger.info(get_achievements(state))
    logger.info("Finished")
