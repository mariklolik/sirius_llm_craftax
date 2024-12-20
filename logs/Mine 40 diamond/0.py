
def mine_diamonds(env):
    # Проверяем, есть ли в инвентаре игрока алмазы
    if check_inventory_diamond(env) == 0:
        # Если алмазов нет, ищем их на карте
        explore_until(env, lambda block: block == DiamondBlockType(), max_iter=25, can_dig=True, can_place=False)

    # Создаем алмазную кирку для добычи алмазов
    act_MAKE_DIAMOND_PICKAXE(env)
  
    # Перемещаемся к ближайшему месту с алмазами
    move_to_pos(env, target_pos=find_nearest_diamond_block(env))

    # Добываем алмазы до тех пор, пока не наберем 40 штук
    while check_inventory_diamond(env) < 40:
      mine_block(env, DiamondBlockType())

    return True
thrown exception: invalid syntax (<string>, line 2)