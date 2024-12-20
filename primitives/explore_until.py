import logging
import typing

import jax
from craftax.craftax.constants import BlockType

from .explore import explore_choose_node
from .move_to_node_smart import gen_graph_smart, move_to_pos
from .utils import find_block_any
from functools import partial

logger = logging.getLogger()


def explore_until(
    env,
    callback: BlockType | typing.Callable[[typing.Any], bool],
    max_iter=25,
    can_dig=False,
    can_place=False,
    prev_pos: jax.numpy.ndarray | None = None,
):
    logger.info(f"exploring...")

    if isinstance(callback, BlockType):
        callback_fn = partial(block_in_obs_callback, block_type=callback)
    elif callable(callback):
        callback_fn = callback
    else:
        raise ValueError(
            "callback should be BlockType or function with env as argument"
        )

    if prev_pos is None:
        prev_pos = env.saved_state.player_position
    for i in range(max_iter):
        logger.debug(f"exploring, step {i}/{max_iter}...")
        if callback_fn(env):
            logger.info(f"Done exploring after {i} iterations.")
            if isinstance(callback, BlockType):
                logger.info(
                    f"Found {callback} in pos {find_block_any(env.saved_state, callback)}."
                )
            break

        G = gen_graph_smart(env.saved_state, can_dig, can_place)
        pos = explore_choose_node(env, G, prev_pos)
        prev_pos = env.saved_state.player_position
        move_to_pos(env, pos, G, can_dig, can_place)

    else:
        logger.info(f"No block found after {max_iter} iterations.")


def block_in_obs_callback(env, block_type: BlockType):
    return find_block_any(env.saved_state, block_type) is not None
