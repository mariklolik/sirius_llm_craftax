
def mine_coal(env):
    # Проверяем количество угля в инвентаре игрока
    coal_count = check_inventory_coal(env)

    if coal_count < 30:
        # Если угля недостаточно, добываем его до достижения нужного количества
        mine_block(
            env,
            BlockType.COAL,
            count=30 - coal_count,
        )
thrown exception: invalid syntax (<string>, line 2)