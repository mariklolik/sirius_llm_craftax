
def craft_torches(env):
    # Проверяем, есть ли в инвентаре игрока необходимые ресурсы для создания факелов
    if check_inventory_coal(env) > 0 and check_inventory_stick(env) > 0:
        # Создаем факелы
        act_PLACE_STONE(env)  # Размещаем каменный блок
        move_to_pos(env, Player_position)
        explore_until(env, lambda x: x == BlockType.COAL, max_iter=25)

        for _ in range(check_inventory_stick(env)):
            act_MAKE_TORCH(env)
    else:
        print("Недостаточно ресурсов для крафта факелов")
thrown exception: invalid syntax (<string>, line 2)