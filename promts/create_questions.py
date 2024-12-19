from craftax.craftax.craftax_state import EnvState
import jax
from craftax.craftax_env import make_craftax_env_from_name

rng = jax.random.PRNGKey(0)
rng, _rng = jax.random.split(rng)
rngs = jax.random.split(_rng, 3)

# Create environment
env = make_craftax_env_from_name("Craftax-Symbolic-v1", auto_reset=True)
env_params = env.default_params

# Get an initial state and observation
obs, state = env.reset(rngs[0], env_params)

# Pick random action
action = env.action_space(env_params).sample(rngs[1])

# Step environment
obs, state, reward, done, info = env.step(rngs[2], state, action, env_params)

def func(state: EnvState, completedTask, failedTask):
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
    text = open("curriculum_qa_step1_ask_questions.txt", "r").read()
    text = text.format(mapBlocks, mapItems, mapLight, playerPosition, playerHealth, playerHunger, playerDrink, playerEnergy, playerLevel, playerMana, isSleeping, isResting, inventory, achievement, completedTask, failedTask)
    return text

f = open("output.txt", "w")

f.write(func(state, [], []))
f.close()