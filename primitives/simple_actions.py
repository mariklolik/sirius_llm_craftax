from craftax.craftax.constants import Action
from primitives.executor import executor
from primitives.checks import check_player_position, check_forward_block
from primitives.move_to_node_smart import move_to_pos


def act_NOOP(env):
    executor(env, [Action.NOOP])


def act_LEFT(env):
    executor(env, [Action.LEFT])


def act_RIGHT(env):
    executor(env, [Action.RIGHT])


def act_UP(env):
    executor(env, [Action.UP])


def act_DOWN(env):
    executor(env, [Action.DOWN])


def act_DO(env):
    executor(env, [Action.DO])


def act_SLEEP(env):
    executor(env, [Action.SLEEP])


def act_PLACE_STONE(env):
    executor(env, [Action.PLACE_STONE])

def act_PLACE_TABLE(env):
    if (check_forward_block(env) != BlockType.CRAFTING_TABLE):
        act_DO(env)
    executor(env, [Action.PLACE_TABLE])

def act_PLACE_FURNACE(env):
    act_UP(env)
    act_DO(env)
    act_UP(env)
    act_DO(env)
    act_UP(env)
    act_DO(env)
    act_PLACE_TABLE(env)
    act_DOWN(env)
    act_DOWN(env)
    act_UP(env)
    executor(env, [Action.PLACE_FURNACE])
    pos = check_player_position(env)
    move_to_pos([pos[0] + 1, pos[1] + 1])

def act_MAKE_WOOD_PICKAXE(env):
    executor(env, [Action.MAKE_WOOD_PICKAXE])


def act_MAKE_STONE_PICKAXE(env):
    executor(env, [Action.MAKE_STONE_PICKAXE])


def act_MAKE_IRON_PICKAXE(env):
    executor(env, [Action.MAKE_IRON_PICKAXE])


def act_MAKE_WOOD_SWORD(env):
    executor(env, [Action.MAKE_WOOD_SWORD])


def act_MAKE_STONE_SWORD(env):
    executor(env, [Action.MAKE_STONE_SWORD])


def act_MAKE_IRON_SWORD(env):
    executor(env, [Action.MAKE_IRON_SWORD])


def act_REST(env):
    executor(env, [Action.REST])


def act_DESCEND(env):
    executor(env, [Action.DESCEND])


def act_ASCEND(env):
    executor(env, [Action.ASCEND])


def act_MAKE_IRON_ARMOUR(env):
    executor(env, [Action.MAKE_IRON_ARMOUR])