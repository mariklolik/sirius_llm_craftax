def format_text_with_state(text, state):
    mapBlocks = state.map[state.player_level].tolist()
    mapItems = state.item_map[state.player_level].tolist()
    mapLight = state.light_map[state.player_level].tolist()
    playerPosition = state.player_position.tolist()
    playerHealth = state.player_health
    playerHunger = state.player_hunger
    playerDrink = state.player_drink
    playerEnergy = state.player_energy
    playerLevel = state.player_level
    playerMana = state.player_mana
    isSleeping = state.is_sleeping
    isResting = state.is_resting
    inventory = state.inventory
    achievement = state.achievements.tolist()
    text = text.format(mapBlocks, mapItems, mapLight, 
                           playerPosition, playerHealth, playerHunger, 
                           playerDrink, playerEnergy, playerLevel, 
                           playerMana, isSleeping, isResting, 
                           inventory, achievement)
    return text