from craftax.craftax.constants import Action
from .executor import executor


def act_DO(env):
    action = Action.DO
    executor(env, [action])

def act_PLACE_STONE(env):
    action = Action.PLACE_STONE
    executor(env, [action])

def act_PLACE_TABLE(env):
    action = Action.PLACE_TABLE
    executor(env, [action])

def act_PLACE_FURNACE(env):
    action = Action.PLACE_FURNACE
    executor(env, [action])

def act_PLACE_PLANT(env):
    action = Action.PLACE_PLANT
    executor(env, [action])

def act_MAKE_WOOD_PICKAXE(env):
    action = Action.MAKE_WOOD_PICKAXE
    executor(env, [action])

def act_MAKE_STONE_PICKAXE(env):
    action = Action.MAKE_STONE_PICKAXE
    executor(env, [action])

def act_MAKE_IRON_PICKAXE(env):
    action = Action.MAKE_IRON_PICKAXE
    executor(env, [action])

def act_MAKE_WOOD_SWORD(env):
    action = Action.MAKE_WOOD_SWORD
    executor(env, [action])

def act_MAKE_STONE_SWORD(env):
    action = Action.MAKE_STONE_SWORD
    executor(env, [action])

def act_MAKE_IRON_SWORD(env):
    action = Action.MAKE_IRON_SWORD
    executor(env, [action])

def act_MAKE_DIAMOND_PICKAXE(env):
    action = Action.MAKE_DIAMOND_PICKAXE
    executor(env, [action])

def act_MAKE_DIAMOND_SWORD(env):
    action = Action.MAKE_DIAMOND_SWORD
    executor(env, [action])

def act_MAKE_IRON_ARMOUR(env):
    action = Action.MAKE_IRON_ARMOUR
    executor(env, [action])

def act_MAKE_DIAMOND_ARMOUR(env):
    action = Action.MAKE_DIAMOND_ARMOUR
    executor(env, [action])