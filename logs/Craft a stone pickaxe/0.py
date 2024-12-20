
def craft_stone_pickaxe(env):
    # Проверяем, есть ли у нас в инвентаре камень
    if check_inventory_stone(env) == 0:
        # Если нет камня, добываем его
        explore_until(env, BlockType.STONE, max_iter=25, can_dig=True, can_place=False)

    # Создаём каменный киркомотыг
    act_MAKE_STONE_PICKAXE(env)
thrown exception: invalid syntax (<string>, line 2)