
def mine_diamonds(env):
    # Проверяем, есть ли в инвентаре игрока алмазная кирка
    if check_inventory_diamond_pickaxe(env) == 0:
        # Если алмазной кирки нет, ищем её на карте
        explore_until(env, lambda block: block == DiamondPickaxeBlockType(), max_iter=25, can_dig=True, can_place=False)

    # Создаём алмазную кирку для добычи алмазов
    act_MAKE_DIAMOND_PICKAXE(env)

    # Перемещаемся к ближайшему месту с алмазами
    move_to_pos(env, target_pos=find_nearest_diamond_block(env))

    # Добываем алмазы до тех пор, пока не наберём 40 штук
    while check_inventory_diamond(env) < 40:
        mine_block(env, DiamondBlockType())

    return True

def check_inventory_diamond_pickaxe(env):
    """Returns the number of diamond pickaxes in the inventory."""
    return env.saved_state.inventory.diamond_pickaxe
thrown exception: invalid syntax (<string>, line 2)