def task_prompt_template(state, completedTask, failedTask, question, answers):
    quest = list(question["result"]['alternatives'][0]['message']['text'].split('\n'))
    text_part1 = open("curriculum_part1.txt").read()
    text_part3 = open("curriculum_part3.txt").read()
    text_part2 = ""

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

    cnt = 0
    for i in range(0, len(quest), 2):
        text_part2 += quest[i] + '\n'
        text_part2 += quest[i + 1] + '\n'
        text_part2 += answers[cnt] + '\n'
        cnt += 1

    text_part3 = text_part3.format(mapBlocks, mapItems, mapLight, playerPosition, playerHealth, playerHunger, playerDrink, playerEnergy, playerLevel, playerMana, isSleeping, isResting, inventory, achievement, completedTask, failedTask)
    return (text_part1 + '\n' + text_part2 + '\n ' + text_part3)
