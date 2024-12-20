import jax
import networkx as nx
from craftax.craftax.craftax_state import EnvState

from primitives.move_to_node_smart import to_node


def explore_choose_node(
    env, G: nx.Graph, prev_pos: jax.numpy.ndarray = None, dist=5
):
    state: EnvState = env.saved_state
    if not to_node(prev_pos) in G.nodes:
        return None
    nodes = jax.numpy.array(list(G.nodes), dtype=jax.numpy.int32)

    direction_vectors = nodes - state.player_position
    distances = jax.numpy.sum(jax.numpy.abs(direction_vectors), axis=1)

    if prev_pos is not None:
        prev_direction = state.player_position - prev_pos[:, jax.numpy.newaxis]

        dot_products = direction_vectors.dot(prev_direction).sum(axis=-1)

        if jax.numpy.any(dot_products >= 0):
            direction_mask = dot_products >= 0
        else:
            direction_mask = dot_products < 0
    else:
        direction_mask = jax.numpy.ones(direction_vectors.shape[0], dtype=bool)

    for cool_distance in range(dist, -1, -1):
        indexes = jax.numpy.where(
            jax.numpy.logical_and(distances == cool_distance, direction_mask)
        )[0]
        if len(indexes) == 0:
            continue
        env.rng, rng = jax.random.split(env.rng)
        idx = jax.random.choice(rng, indexes)
        return nodes[idx]
    return None
