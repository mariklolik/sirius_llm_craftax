from craftax.craftax.constants import Action
import os

from .wrapper import SaveStateWrapper
import logging

logger = logging.getLogger("Executor")


def executor(env: SaveStateWrapper, action_list: list[Action]):
    # append acton_list to actions.csv
    action_log_file = os.path.join(env.log_dir, "actions.txt")
    logger.info(f"acting: {action_list}")
    with open(action_log_file, "a+") as f:
        for action in action_list:
            f.write(f"{action.value}\n")

    # execute actions
    for action in action_list:
        obs, state, reward, done, info = env.step(action)
