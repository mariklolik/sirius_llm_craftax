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


def act_PLACE_PLANT(env):
    executor(env, [Action.PLACE_PLANT])


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


def act_MAKE_DIAMOND_PICKAXE(env):
    executor(env, [Action.MAKE_DIAMOND_PICKAXE])


def act_MAKE_DIAMOND_SWORD(env):
    executor(env, [Action.MAKE_DIAMOND_SWORD])


def act_MAKE_IRON_ARMOUR(env):
    executor(env, [Action.MAKE_IRON_ARMOUR])


def act_MAKE_DIAMOND_ARMOUR(env):
    executor(env, [Action.MAKE_DIAMOND_ARMOUR])


def act_SHOOT_ARROW(env):
    executor(env, [Action.SHOOT_ARROW])


def act_MAKE_ARROW(env):
    executor(env, [Action.MAKE_ARROW])


def act_CAST_FIREBALL(env):
    executor(env, [Action.CAST_FIREBALL])


def act_CAST_ICEBALL(env):
    executor(env, [Action.CAST_ICEBALL])


def act_PLACE_TORCH(env):
    executor(env, [Action.PLACE_TORCH])


def act_DRINK_POTION_RED(env):
    executor(env, [Action.DRINK_POTION_RED])


def act_DRINK_POTION_GREEN(env):
    executor(env, [Action.DRINK_POTION_GREEN])


def act_DRINK_POTION_BLUE(env):
    executor(env, [Action.DRINK_POTION_BLUE])


def act_DRINK_POTION_PINK(env):
    executor(env, [Action.DRINK_POTION_PINK])


def act_DRINK_POTION_CYAN(env):
    executor(env, [Action.DRINK_POTION_CYAN])


def act_DRINK_POTION_YELLOW(env):
    executor(env, [Action.DRINK_POTION_YELLOW])


def act_READ_BOOK(env):
    executor(env, [Action.READ_BOOK])


def act_ENCHANT_SWORD(env):
    executor(env, [Action.ENCHANT_SWORD])


def act_ENCHANT_ARMOUR(env):
    executor(env, [Action.ENCHANT_ARMOUR])


def act_MAKE_TORCH(env):
    executor(env, [Action.MAKE_TORCH])


def act_LEVEL_UP_DEXTERITY(env):
    executor(env, [Action.LEVEL_UP_DEXTERITY])


def act_LEVEL_UP_STRENGTH(env):
    executor(env, [Action.LEVEL_UP_STRENGTH])


def act_LEVEL_UP_INTELLIGENCE(env):
    executor(env, [Action.LEVEL_UP_INTELLIGENCE])


def act_ENCHANT_BOW(env):
    executor(env, [Action.ENCHANT_BOW])
