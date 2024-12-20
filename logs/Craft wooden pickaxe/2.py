
def craft_wooden_pickaxe(env):
    # Проверяем, есть ли у игрока в инвентаре деревянная кирка или более качественное орудие.
    if check_inventory_wood_pickaxe(env) == False:
        # Если нет, проверяем количество древесины в инвентаре.
        wood_amount = check_inventory_wood(env)
        if wood_amount >= 3:
            # Если есть древесина, используем её для создания деревянной кирки.
            act_MAKE_WOOD_SWORD(env)  # Создаём деревянный меч как промежуточный этап.

            # Используем печь для переплавки древесины в палки.
            explore_until(env, lambda x: x == BlockType.STONE_BRICK_FURNACE, max_iter=25)
            act_PLACE_FURNACE(env)  # Размещаем печь.

            for _ in range(wood_amount):
                # Переплавляем древесину в палки.
                act_MAKE_STICKS(env)

            # Создаём деревянную кирку из палок.
            act_MAKE_WOODEN_PICKAXE(env)
    else:
        print("У вас уже есть деревянная кирка или лучше.")
thrown exception: invalid syntax (<string>, line 2)