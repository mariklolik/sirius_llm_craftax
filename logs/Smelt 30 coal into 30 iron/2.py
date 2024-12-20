
def smelt_coal_to_iron(env):
    # Проверяем наличие печи
    furnace_present = act_IS_PRESENT_FURNACE(env)
    if not furnace_present:
        # Размещаем печь, если её нет
        move_to_pos(env, target_pos=(24, 24), G=None, can_dig=True, can_place=True)
        act_PLACE_FURNACE(env)

    # Переплавляем уголь в железо
    while True:
        if not act_MAKE_IRON_ARMOUR(env):  # Используем печь для переплавки угля
            print("Ошибка при переплавке угля")
            return False
        elif env.saved_state.inventory.iron >= 30:  # Проверяем, получили ли мы нужное количество железа
            break

    return True
thrown exception: invalid syntax (<string>, line 2)