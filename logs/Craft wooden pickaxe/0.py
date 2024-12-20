
def craft_wooden_pickaxe(env):
    # Проверяем, есть ли у игрока в инвентаре деревянная кирка или более качественное орудие.
    if check_inventory_wood_pickaxe(env) == False:
        # Если нет, проверяем количество древесины в инвентаре.
        wood_amount = check_inventory_wood(env)
        if wood_amount >= 1:
            # Если есть древесина, используем её для создания деревянной кирки.
            act_MAKE_WOOD_SWORD(env)  # Создаём деревянный меч как промежуточный этап.
            move_to_pos(env, Player_position)  # Возвращаемся на исходную позицию.

            # Используем печь для переплавки деревянного меча в деревянную кирку.
            act_PLACE_FURNACE(env)
            executor(env, [Action.USE_FURNACE, Action.INSERT_WOODEN_SWORD, Action.CRAFT_PICKAXE])

            # Проверяем успешность создания кирки и обновляем инвентарь.
            if env.saved_state.inventory.pickaxe >= 1:
                print("Деревянная кирка создана!")
            else:
                print("Ошибка при создании кирки.")
        else:
            print("Недостаточно древесины для создания кирки.")
    else:
        print("У вас уже есть деревянная кирка или лучше.")
thrown exception: invalid syntax (<string>, line 2)