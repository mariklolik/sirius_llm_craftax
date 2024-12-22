from primitives import visual
from primitives.wrapper import SaveStateWrapper
from craftax.craftax_env import make_craftax_env_from_name
SEED = 123
env = SaveStateWrapper(make_craftax_env_from_name("Craftax-Symbolic-v1", auto_reset=False), SEED, "logs")
env.reset()
visual.visualise_actions(env, "logs/actions.txt")