import importlib
import logging
import sys
import os

from craftax.craftax_env import make_craftax_env_from_name
from primitives.wrapper import SaveStateWrapper

from skills.utils import init_db

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)

SEED = 0xBAD_5EED_B00B5

def env_to_prompt(env):
    return NotImplementedError

def envoke_action(env, act):
    return NotImplementedError

def log_metrics(env):
    return NotImplementedError



if __name__ == "__main__":

    init_db()

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger('main_logger')
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)

    env = make_craftax_env_from_name("Craftax-Symbolic-v1", auto_reset=False)
    env = SaveStateWrapper(env, seed=SEED, log_dir="./logs")
    obs, state = env.reset()

    with open(log_dir + '/actions.txt', 'w') as f:
        pass

    logger.info('Started')

    game_finished = False

    while not game_finished:
        # prompt = env_to_prompt()
        # task = gpt(prompt - придумай task)
        # action_source = gpt(task + prompt) спрашиваем как в текущих условиях решить поставлениную задачу
        # action_working = validate(action_source)
        # if action_working:
        #   add_action_to_db(action_source)
        # 
        # calc cosine_similarity(task, all_sources_in_db)
        # actions = choose top-p = 0.5 actions
        # for act in actions:
        #   envoke_action(env, act)
        #  
        pass
        
    
    logger.info('Finished')