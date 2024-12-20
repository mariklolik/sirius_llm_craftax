
def mine_wood(env):
    # Проверяем, есть ли у игрока в инвентаре деревянная кирка или более качественное орудие.
    if not check_inventory_wood_pickaxe(env):
        # Если нет, то создаём деревянный киркомолот.
        act_MAKE_WOOD_PICKAXE(env)

    # Получаем количество древесины в инвентаре игрока.
    wood_count = check_inventory_wood(env)
  
    # Определяем, сколько раз нужно ударить по дереву, чтобы добыть необходимое количество древесины
    iterations = 10 if wood_count == 0 else 10 // wood_count
    
    # Добываем необходимое количество древесины
    while iterations > 0:
        explore_until(env, lambda pos: pos[0] == Player_position[0] and pos[1] == Player_position[1], max_iter=5, can_dig=True, can_place=False)
        mine_block(env, BlockType.WOOD, count=1, max_iter=25, can_dig=True)
        iterations -= 1

    print("Добыто древесины:", wood_count)

# Функция для проверки количества древесины в инвентаре.
def check_inventory_wood(env):
    return env.saved_state.inventory.wood

# Функция, проверяющая, есть ли у игрока в инвентаре деревянная кирка или более качественное орудие.
def check_inventory_wood_pickaxe(env) -> bool:
    return env.saved_state.inventory.pickaxe >= 1

# Создание деревянного киркомолота, что позволяет игроку эффективнее добывать ресурсы в подземелье
def act_MAKE_WOOD_PICKAXE(env):
    executor(env, [Action.MAKE_WOOD_PICKAXE])

# Выполнение функции
mine_wood(env)
thrown exception: invalid syntax (<string>, line 2)