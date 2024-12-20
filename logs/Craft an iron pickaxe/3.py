
def craft_iron_pickaxe(env):
    # Проверяем, есть ли у нас железо
    if check_inventory_iron(env) == 0:
        # Если нет, ищем железо с помощью explore_until
        explore_until(env, 'iron', max_iter=25, can_dig=False, can_place=False)

    # Если у нас есть железо, идём к печи
    move_to_pos(env, env.saved_state.Player_position)
    act_PLACE_FURNACE(env)

    # Создаём железную кирку
    act_MAKE_IRON_PICKAXE(env)
thrown exception: invalid syntax (<string>, line 2)