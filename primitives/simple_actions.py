from craftax.craftax.constants import Action
from primitives.executor import executor


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
    executor(env, [Action.PLACE_TABLE])

def act_PLACE_FURNACE(env):
    executor(env, [Action.PLACE_FURNACE])

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

from craftax.craftax.constants import DIRECTIONS, BlockType
from craftax.craftax.craftax_state import EnvState

## ITEMS


def check_inventory_wood(env):
    """Returns the number of wood in the inventory."""
    return env.saved_state.inventory.wood


def check_inventory_stone(env):
    """Returns the number of stone in the inventory."""
    return env.saved_state.inventory.stone


def check_inventory_coal(env):
    """Returns the number of coal in the inventory."""
    return env.saved_state.inventory.coal


def check_inventory_iron(env):
    """Returns the number of iron in the inventory."""
    return env.saved_state.inventory.iron


def check_inventory_diamond(env):
    """Returns the number of diamonds in the inventory."""
    return env.saved_state.inventory.diamond


def check_inventory_bow(env):
    """Returns the number of bows in the inventory."""
    return env.saved_state.inventory.bow


def check_inventory_arrows(env):
    """Returns the number of arrows in the inventory."""
    return env.saved_state.inventory.arrows


def check_inventory_torches(env):
    """Returns the number of torches in the inventory."""
    return env.saved_state.inventory.torches


def check_inventory_ruby(env):
    """Returns the number of rubies in the inventory."""
    return env.saved_state.inventory.ruby


def check_inventory_sapphire(env):
    """Returns the number of sapphires in the inventory."""
    return env.saved_state.inventory.sapphire


def check_inventory_books(env):
    """Returns the number of books in the inventory."""
    return env.saved_state.inventory.books


## PICKAXES


def check_inventory_wood_pickaxe(env) -> bool:
    """Returns True if the player has a wood pickaxe or better in the inventory, False otherwise."""
    return env.saved_state.inventory.pickaxe >= 1


def check_inventory_stone_pickaxe(env) -> bool:
    """Returns True if the player has a stone pickaxe or better in the inventory, False otherwise."""
    return env.saved_state.inventory.pickaxe >= 2


def check_inventory_iron_pickaxe(env) -> bool:
    """Returns True if the player has a iron pickaxe or better in the inventory, False otherwise."""
    return env.saved_state.inventory.pickaxe >= 3


def check_inventory_diamond_pickaxe(env) -> bool:
    """Returns True if the player has a diamond pickaxe or better in the inventory, False otherwise."""
    return env.saved_state.inventory.pickaxe >= 4


## SWORDS


def check_inventory_wood_sword(env) -> bool:
    """Returns True if the player has a wood sword or better in the inventory, False otherwise."""
    return env.saved_state.inventory.sword >= 1


def check_inventory_stone_sword(env) -> bool:
    """Returns True if the player has a stone sword or better in the inventory, False otherwise."""
    return env.saved_state.inventory.sword >= 2


def check_inventory_iron_sword(env) -> bool:
    """Returns True if the player has a iron sword or better in the inventory, False otherwise."""
    return env.saved_state.inventory.sword >= 3


def check_inventory_diamond_sword(env) -> bool:
    """Returns True if the player has a diamond sword or better in the inventory, False otherwise."""
    return env.saved_state.inventory.sword >= 4


## BLOCK ON MAP


def check_forward_block(env) -> BlockType:
    state: EnvState = env.saved_state
    pos = state.player_position + DIRECTIONS[state.player_direction]
    return BlockType(state.map[state.player_level][pos[0], pos[1]])
