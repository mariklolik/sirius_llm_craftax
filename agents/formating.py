def distans(x1, y1, x2, y2):
    if abs(x1 - x2) <= 5 and abs(y1 - y2) <= 5:
        return True
    return False

def format_text_with_state(text: str, state, *args):
    player_health = state.player_health
    player_hunger = state.player_hunger
    player_drink = state.player_drink
    player_energy = state.player_energy
    is_sleeping = state.is_sleeping
    inventory = state.inventory.__dict__
    inv = {}
    for key, value in inventory.items():
        value = value.tolist()
        if isinstance(value, int) and key != "sapling":
            if value > 0:
                inv[key] = value
    text = text.format(
        player_health,
        player_hunger,
        player_drink,
        player_energy,
        is_sleeping,
        inv,
        *args
    )
    return text
