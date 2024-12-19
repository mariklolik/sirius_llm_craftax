import importlib
import logging
import sys
import os

from skills.utils import init_db
from game import create_env, get_achievements

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)

SEED = 0xBAD_5EED_B00B5

def state_to_prompt(state):
    return NotImplementedError

def envoke_action(state, code):
    func = eval(code)
    obs, state, reward, done, info = func(state)
    return state, done

def log_metrics(state):
    return NotImplementedError


if __name__ == "__main__":

    init_db()

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger('main_logger')
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)

    state = create_env(SEED)

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
        #   action_desc = gpt3.5(action_source) # получаем описание
        #
        #   add_action_to_db(action_source, action_desc) #emb считаем по описанию, кладем в базу исходник
        # 
        # calc cosine_similarity(task, all_sources_in_db)
        # actions = choose top-p = 0.5 actions
        # for act in actions:
        #   env, done = envoke_action(env, act)
        #   if done:
        #       info, rewards = get_achievements(env)
        #       break
        #
        #  
        pass
        
    log_metrics(state)
    logger.info('Finished')
