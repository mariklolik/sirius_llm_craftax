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

def func(state: EnvState, final_task):
    inventory = state.inventory

    text = open("curriculum_task_decomposition.txt", "r").read()
    text = text.format(inventory, final_task)
    return text

f = open("output.txt", "w")

f.write(func(state, "Собрать 5 штук дерева"))
f.close()