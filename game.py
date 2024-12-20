from craftax.craftax_env import make_craftax_env_from_name
from craftax.craftax.constants import (
    Achievement,
    INTERMEDIATE_ACHIEVEMENTS,
    VERY_ADVANCED_ACHIEVEMENTS,
)
from primitives.wrapper import SaveStateWrapper


def create_env(seed=0xBAD_5EED_B00B5):
    env = make_craftax_env_from_name("Craftax-Symbolic-v1", auto_reset=False)
    env_params = env.default_params
    env = SaveStateWrapper(env, seed=seed, log_dir="./logs")
    obs, state = env.reset()
    return state


def achievement_mapping(achievement_value):
    if achievement_value <= 24:
        return 1
    elif achievement_value in INTERMEDIATE_ACHIEVEMENTS:
        return 3
    elif achievement_value in VERY_ADVANCED_ACHIEVEMENTS:
        return 8
    else:
        return 5


def get_achievements(state):
    achievements = state.achievements
    info = {}
    sum_rewards = 0
    for achievement in Achievement:
        name = " ".join(achievement.name.capitalize().split("-"))
        info[name] = int(
            achievements[achievement.value]
        ) * achievement_mapping(achievement.value)
        sum_rewards += info[name]
    return info, sum_rewards
