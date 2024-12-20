
def mine_coal(env):
    # Проверяем, есть ли у игрока уголь в инвентаре
    if check_inventory_coal(env) == 0:
        # Если угля нет, ищем его на карте
        explore_until(
            env,
            callback=BlockType.COAL,
            max_iter=25,
            can_dig=True,
            can_place=False,
        )

    # Создаём алмазный киркомотыг для более эффективной добычи угля
    act_MAKE_DIAMOND_PICKAXE(env)
    logger.info("Создан алмазный киркомотыг")

    # Добываем уголь
    mine_block(
        env,
        BlockType.COAL,
        count=10,
        max_iter=25,
        can_dig=True,
        can_place=False,
    )
    logger.debug("Закончена добыча угля")
thrown exception: invalid syntax (<string>, line 2)