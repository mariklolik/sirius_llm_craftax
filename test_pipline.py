import importlib
import logging
import sys
import os

from src.primitives.checks import check_inventory_wood
from src.primitives.mine_block import mine_block
from src.primitives.simple_actions import act_PLACE_TABLE, act_MAKE_WOOD_PICKAXE, act_DO, act_PLACE_FURNACE, \
    act_MAKE_IRON_SWORD, act_MAKE_STONE_PICKAXE, act_MAKE_IRON_PICKAXE

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)

from craftax.craftax.constants import BlockType
from craftax.craftax_env import make_craftax_env_from_name
import craftax.craftax.renderer as renderer

from src.primitives.explore import explore_choose_node
from src.primitives.gifs import visual_testing
from src.primitives.move_to_node_smart import gen_graph_smart, move_to_pos
from src.primitives.utils import find_block_any, find_block_all
from src.primitives.wrapper import SaveStateWrapper

SEED = 0xBAD_5EED_B00B5

def explore_and_chop(env: SaveStateWrapper, block_type: BlockType, max_iter = 25, can_dig=False, can_place=False):
    prev_pos = env.saved_state.player_position

    for i in range(max_iter):
        if find_block_any(env.saved_state, block_type) is not None:
            break
        G = gen_graph_smart(env.saved_state, can_dig, can_place)
        pos = explore_choose_node(env, G, prev_pos)
        prev_pos = env.saved_state.player_position
        move_to_pos(env, pos, G, can_dig, can_place)
    else:
        print('no block found')
        return

    targets = find_block_all(env.saved_state, block_type)
    closest_target_index = abs(targets - env.saved_state.player_position).sum(axis=-1).argmin()
    closest_target = targets[closest_target_index]
    move_to_pos(env, closest_target, can_dig=can_dig, can_place=can_place)
    act_DO(env)

if __name__ == '__main__':
    importlib.reload(renderer)

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger('main_logger')
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)

    env = make_craftax_env_from_name("Craftax-Symbolic-v1", auto_reset=False)
    env = SaveStateWrapper(env, seed=SEED, log_dir=log_dir)
    obs, state = env.reset()

    with open(log_dir + '/actions.txt', 'w') as f:
        pass

    logger.info('Started')

    ### do some stuff
    mine_block(env, BlockType.TREE, 8, can_dig=False, can_place=False)
    if not check_inventory_wood(env):
        logging.error('No wood found!')
    # for i in range(8):
    #     explore_and_chop(env, BlockType.TREE, can_dig=False, can_place=False)

    act_PLACE_TABLE(env)
    act_MAKE_WOOD_PICKAXE(env)

    mine_block(env, BlockType.STONE, 5, can_dig=True, can_place=False)
    # for i in range(5):
    #     explore_and_chop(env, BlockType.STONE, can_dig=True, can_place=False)

    act_PLACE_TABLE(env)
    act_MAKE_STONE_PICKAXE(env)

    mine_block(env, BlockType.COAL, 3, can_dig=True, can_place=False)
    # for i in range(3):
    #     explore_and_chop(env, BlockType.COAL, can_dig=True, can_place=False)

    mine_block(env, BlockType.TREE, 3, can_dig=True, can_place=False)
    # for i in range(3):
    #     explore_and_chop(env, BlockType.TREE)

    mine_block(env, BlockType.IRON, 2, can_dig=True, can_place=False)
    # for i in range(2):
    #     explore_and_chop(env, BlockType.IRON, can_dig=True, can_place=False)

    act_PLACE_FURNACE(env)
    mine_block(env, BlockType.STONE, can_dig=True, can_place=False)

    act_PLACE_TABLE(env)
    act_MAKE_IRON_SWORD(env)
    act_MAKE_IRON_PICKAXE(env)

    mine_block(env, BlockType.WATER, can_dig=True, can_place=True)

    for i in range(5):
        act_DO(env)

    # # Render
    logger.info('Rendering...')

    visual_testing(SEED, log_dir + '/actions.txt', log_dir, 1, env, renderer,
                   grid_size=(1, 1))

    logger.info('Finished')