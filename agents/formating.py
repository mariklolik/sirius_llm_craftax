def format_text_with_state(text: str, state, *args):
    map_blocks = state.map[state.player_level].tolist()
    player_position = state.player_position.tolist()
    # Assuming player_position is a list [x, y]
    player_x, player_y = player_position

    # Get the dimensions of the map
    map_height = len(map_blocks)
    map_width = len(map_blocks[0])

    # Calculate the boundaries of the 5x5 sub-map with edge case handling
    start_x = max(0, player_x - 5)
    start_y = max(0, player_y - 5)
    end_x = min(map_width, player_x + 6)
    end_y = min(map_height, player_y + 6)

    # Extract the 5x5 sub-map
    sub_map = [row[start_x:end_x] for row in map_blocks[start_y:end_y]]

    # Print the sub-map
    map_blocks = sub_map
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
    achievement = str(state.achievements.tolist())
    text = text.format(
        map_blocks,
        [],
        [],
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
        *args
    )
    return text
