def distans(x1, y1, x2, y2):
    if abs(x1 - x2) <= 5 and abs(y1 - y2) <= 5:
        return True
    return False

def format_text_with_state(text: str, state, *args):
    map_blocks = state.map[state.player_level].tolist()
    player_position = state.player_position.tolist()
    player_x, player_y = player_position

    map_height = len(map_blocks)
    map_width = len(map_blocks[0])

    start_x = max(0, player_x - 5)
    start_y = max(0, player_y - 5)
    end_x = min(map_width, player_x + 6)
    end_y = min(map_height, player_y + 6)

    sub_map = [row[start_x:end_x] for row in map_blocks[start_y:end_y]]

    map_blocks = sub_map
    map_items = state.item_map[state.player_level].tolist()
    
    coord_ladder_down = "Need to find"
    coord_ladder_up = "Need to find"
    ladder_down_is_blocked = ""

    for x in range(len(map_items)):
        for y in range(len(map_items[0])):
            if distans(x, y, player_x, player_y):
                if map_items[x][y] == 2:
                    coord_ladder_down = (x, y)
                if map_items[x][y] == 3:
                    coord_ladder_up = (x, y)
                if map_items[x][y] == 4:
                    coord_ladder_down = (x, y)
                    ladder_down_is_blocked = "Ladder down is blocked, need to kill more mobs"

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
    text = text.format(
        map_blocks,
        coord_ladder_down, 
        ladder_down_is_blocked,
        coord_ladder_up,
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
        *args
    )
    return text
