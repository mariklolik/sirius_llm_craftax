
def craft_furnace(env):
    # Проверяем, есть ли у нас уголь
    if check_inventory_coal(env) < 8:
        explore_until(env, BlockType.COAL, max_iter=25, can_dig=False, can_place=False)

    # Добываем уголь
    mine_block(env, BlockType.COAL, count=8, max_iter=25, can_dig=True, can_place=False)
  
    # Проверяем наличие железа
    if check_inventory_iron(env) < 1:
        explore_until(env, BlockType.IRON_ORE, max_iter=25, can_dig=True, can_place=False)
      
    # Добываем железо
    mine_block(env, BlockType.IRON_ORE, count=1, max_iter=25, can_dig=True, can_place=False)
   
    # Создаём железный киркомотыг
    act_MAKE_IRON_PICKAXE(env)
     
    # Используем железный киркомотыг для добычи камня
    move_to_pos(env, target_pos=(24, 24))
    explore_until(env, BlockType.STONE, max_iter=25, can_dig=True, can_place=False)
    
    # Строим печь
    act_PLACE_FURNACE(env)
thrown exception: invalid syntax (<string>, line 2)