def format_text_with_state(text: str, state):
    map_blocks = state.map[state.player_level].tolist()
    map_items = state.item_map[state.player_level].tolist()
    map_light = state.light_map[state.player_level].tolist()
    player_position = state.player_position.tolist()
    player_health = state.player_health
    player_hunger = state.player_hunger
    player_drink = state.player_drink
    player_energy = state.player_energy
    player_level = state.player_level
    player_mana = state.player_mana
    is_sleeping = state.is_sleeping
    is_resting = state.is_resting
    inventory = state.inventory
    achievement = state.achievements.tolist()
    text = text.format(
        map_blocks,
        map_items,
        map_light,
        player_position,
        player_health,
        player_hunger,
        player_drink,
        player_energy,
        player_level,
        player_mana,
        is_sleeping,
        is_resting,
        inventory,
        achievement,
    )
    return text
