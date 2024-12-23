import logging

from craftax.craftax.constants import BlockType

from primitives.explore_until import explore_until
from primitives.move_to_node_smart import move_to_pos
from primitives.simple_actions import act_DO
from primitives.utils import find_block_all

logger = logging.getLogger()


def find_and_mine_block(
    env,
    block_type: BlockType,
    count: int = 1,
    max_iter=25
):
    logger.info(f"mining {count } of {block_type}...")
    for block_iteration in range(count):
        logger.debug(f"iteration {block_iteration}/{count} of find_block...")
        explore_until(
            env,
            callback=block_type,
            max_iter=max_iter
        )

        targets = find_block_all(env.saved_state, block_type)
        if len(targets) == 0:
            continue

        closest_target_index = (
            abs(targets - env.saved_state.player_position)
            .sum(axis=-1)
            .argmin()
        )
        closest_target = targets[closest_target_index]
        move_to_pos(env, closest_target)
        act_DO(env)
    logger.debug(f"Finished mining of {block_type}.")
