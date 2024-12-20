
def craft_stone_pickaxe(env):
    # Проверяем, есть ли у нас в инвентаре камень и дерево
    if check_inventory_stone(env) == 0 or check_inventory_wood(env) == 0:
        # Если нет камня или дерева, добываем их
        explore_until(env, BlockType.STONE | BlockType.WOOD, max_iter=25, can_dig=True, can_place=False)

    # Создаём каменный киркомотыг
    act_MAKE_STONE_PICKAXE(env)

# Функция для проверки наличия камня в инвентаре
def check_inventory_stone(env):
    return env.saved_state.inventory.stone

# Функция для проверки наличия дерева в инвентаре
def check_inventory_wood(env):
    return env.saved_state.inventory.wood

# Создание каменного киркомотыга
def act_MAKE_STONE_PICKAXE(env):
    executor(env, [Action.MAKE_STONE_PICKAXE])
thrown exception: invalid syntax (<string>, line 2)