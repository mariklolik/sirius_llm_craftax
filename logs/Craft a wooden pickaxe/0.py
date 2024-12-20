
def craft_wooden_pickaxe(env):
    # Проверяем, есть ли у игрока в инвентаре деревянная кирка или более качественное орудие.
    if check_inventory_wood_pickaxe(env) == False:
        # Если нет, проверяем количество древесины в инвентаре.
        wood_amount = check_inventory_wood(env)
        if wood_amount >= 1:
            # Если есть древесина, используем её для создания деревянной кирки.
            act_PLACE_FURNACE(env)  # Размещаем печь.
            move_to_pos(env, Player_position)  # Перемещаемся к печи.

            # Создаём деревянную кирку.
            for _ in range(wood_amount):
                mine_block(env, BlockType.WOOD)  # Добываем древесину.
                act_MAKE_WOODEN_PICKAXE(env)

    return env
thrown exception: invalid syntax (<string>, line 2)