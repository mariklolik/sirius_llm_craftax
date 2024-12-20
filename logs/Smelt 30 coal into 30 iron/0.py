
def smelt_coal_to_iron(env):
    # Проверяем количество угля в инвентаре игрока
    coal_count = env.saved_state.inventory.coal

    if coal_count < 30:
        # Если угля недостаточно, ищем его на карте
        explore_until(env, BlockType.COAL, max_iter=25, can_dig=False, can_place=False)

        # Перемещаемся к печи (если она есть) или размещаем её
        move_to_pos(env, target_pos=(24, 24), G=None, can_dig=True, can_place=True)
        act_PLACE_FURNACE(env)

        # Переплавляем уголь в железо
        for _ in range(30):
            if not act_MAKE_IRON_ARMOUR(env):  # Используем печь для переплавки угля
                print("Ошибка при переплавке угля")
                return False

        return True
    else:
        print("У вас уже достаточно угля для выполнения задачи")
        return False
thrown exception: invalid syntax (<string>, line 2)