
def craft_diamond_pickaxe(env):
    # Проверяем, есть ли у игрока алмазы в инвентаре
    if check_inventory_diamond(env) == 0:
        # Если алмазов нет, ищем их
        explore_until(env, lambda block: block == DiamondBlockType(), max_iter=25, can_dig=False, can_place=False)

    # Создаём алмазный меч, если его ещё нет
    if not check_inventory_diamond_sword(env):
        act_MAKE_DIAMOND_SWORD(env)

    # Используем алмазный меч для добычи алмазов
    mine_block(env, DiamondBlockType())

    # Создаём алмазную кирку
    act_MAKE_DIAMOND_PICKAXE(env)

    # Добавляем алмазную кирку в инвентарь
    env.saved_state.inventory.diamond_pickaxe += 1
thrown exception: invalid syntax (<string>, line 2)