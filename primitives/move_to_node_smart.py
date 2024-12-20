from queue import Queue

import jax
import networkx as nx
from craftax.craftax.constants import DIRECTIONS, BlockType, Action
from craftax.craftax.craftax_state import EnvState

from .utils import get_obs_mask, is_in_obs
from .executor import executor

DIRECTIONS_TO_ACTIONS = {
    (0, 0): Action.NOOP,
    (0, -1): Action.LEFT,
    (0, 1): Action.RIGHT,
    (-1, 0): Action.UP,
    (1, 0): Action.DOWN,
}


def to_node(pos: jax.numpy.ndarray):
    return pos[0].item(), pos[1].item()


INF_WEIGHT = 10**6
BLOCK_WEIGHT = {
    BlockType.INVALID: INF_WEIGHT,
    BlockType.OUT_OF_BOUNDS: INF_WEIGHT,
    BlockType.GRASS: 1,
    BlockType.WATER: 15,
    BlockType.STONE: 10,
    BlockType.TREE: 10,
    BlockType.WOOD: 10,
    BlockType.PATH: 1,
    BlockType.COAL: 10,
    BlockType.IRON: 10,
    BlockType.DIAMOND: 10,
    BlockType.CRAFTING_TABLE: 15,
    BlockType.FURNACE: 15,
    BlockType.SAND: 1,
    BlockType.LAVA: 15,
    # пока не работаем с этим
    BlockType.PLANT: INF_WEIGHT,
    BlockType.RIPE_PLANT: INF_WEIGHT,
    BlockType.WALL: INF_WEIGHT,
    BlockType.DARKNESS: INF_WEIGHT,
    BlockType.WALL_MOSS: INF_WEIGHT,
    BlockType.STALAGMITE: INF_WEIGHT,
    BlockType.SAPPHIRE: INF_WEIGHT,
    BlockType.RUBY: INF_WEIGHT,
    BlockType.CHEST: INF_WEIGHT,
    BlockType.FOUNTAIN: INF_WEIGHT,
    BlockType.FIRE_GRASS: INF_WEIGHT,
    BlockType.ICE_GRASS: INF_WEIGHT,
    BlockType.GRAVEL: INF_WEIGHT,
    BlockType.FIRE_TREE: INF_WEIGHT,
    BlockType.ICE_SHRUB: INF_WEIGHT,
    BlockType.ENCHANTMENT_TABLE_FIRE: INF_WEIGHT,
    BlockType.ENCHANTMENT_TABLE_ICE: INF_WEIGHT,
    BlockType.NECROMANCER: INF_WEIGHT,
    BlockType.GRAVE: INF_WEIGHT,
    BlockType.GRAVE2: INF_WEIGHT,
    BlockType.GRAVE3: INF_WEIGHT,
    BlockType.NECROMANCER_VULNERABLE: INF_WEIGHT,
}

NEED_DIG = [
    BlockType.STONE,
    BlockType.COAL,
    BlockType.IRON,
    BlockType.DIAMOND,
    BlockType.CRAFTING_TABLE,
    BlockType.FURNACE,
    BlockType.WOOD,
]

NEED_CHOP = [BlockType.TREE]

NEED_PLACE = [BlockType.WATER, BlockType.LAVA]


def gen_graph_smart(
    state: EnvState, can_dig=False, can_place=False
) -> nx.DiGraph:
    mask = get_obs_mask(state)
    start_pos = state.player_position
    level = state.player_level

    G = nx.DiGraph()
    G.add_node(
        to_node(start_pos),
        block_type=BlockType(
            state.map[level][start_pos[0], start_pos[1]].item()
        ),
    )

    q = Queue()
    q.put(start_pos)
    # for y_offset in range(-OBS_DIM[0] // 2, OBS_DIM[0] // 2 + 1):
    #     for x_offset in range(-OBS_DIM[1] // 2, OBS_DIM[1] // 2 + 1):
    while not q.empty():
        # cur_pos = start_pos + jax.numpy.array([y_offset, x_offset])
        cur_pos = q.get()
        cur_node = to_node(cur_pos)

        for direction in DIRECTIONS[1:5]:
            neighbor = cur_pos + direction
            neighbor_node = to_node(neighbor)
            neighbor_type: BlockType = BlockType(
                state.map[level][neighbor[0], neighbor[1]].item()
            )

            if not is_in_obs(state, neighbor, mask, level):
                continue
            if neighbor_type in NEED_DIG and not can_dig:
                continue
            if neighbor_type in NEED_PLACE and not can_place:
                continue

            if neighbor_node not in G.nodes():
                q.put(neighbor)
            weight = BLOCK_WEIGHT[neighbor_type]
            G.add_node(neighbor_node, block_type=neighbor_type)
            G.add_edge(
                cur_node, neighbor_node, weight=weight, direction=direction
            )

    return G


def move_to_node_planner(
    state: EnvState, G: nx.DiGraph, target_node: tuple[int, int]
) -> list[Action]:
    if not target_node in G.nodes:
        return []

    nodes = nx.dijkstra_path(
        G, source=to_node(state.player_position), target=target_node
    )

    actions = []
    for i in range(len(nodes) - 1):
        cur_node, next_node = nodes[i], nodes[i + 1]

        direction: tuple[int, int] = G.edges[cur_node, next_node][
            "direction"
        ].tolist()
        direction = tuple(direction)
        block_type: BlockType = G.nodes[next_node]["block_type"]

        actions.append(
            DIRECTIONS_TO_ACTIONS[direction]
        )  # либо разворот в непроходимый блок, либо движение в проходимый

        if (
            block_type in NEED_DIG and next_node != target_node
        ):  # только если это препятствие на пути, а не конечная цель
            actions.append(Action.DO)  # убрать и пройти
            actions.append(DIRECTIONS_TO_ACTIONS[direction])

        if (
            block_type in NEED_PLACE and next_node != target_node
        ):  # только если это препятствие на пути, а не конечная цель
            actions.append(
                Action.PLACE_STONE
            )  # поставить блок и пройти на него
            actions.append(DIRECTIONS_TO_ACTIONS[direction])

        if (
            block_type in NEED_CHOP and next_node != target_node
        ):  # только если это препятствие на пути, а не конечная цель
            actions.append(Action.DO)  # собрать блок и пройти на его место
            actions.append(DIRECTIONS_TO_ACTIONS[direction])

    return actions


def move_to_pos(
    env,
    target_pos: jax.numpy.ndarray,
    G: nx.DiGraph = None,
    can_dig=False,
    can_place=False,
):
    state = env.saved_state

    if G is None:
        G = gen_graph_smart(state, can_dig, can_place)

    # print(*G.nodes(), sep='\n', end='\n\n')
    target_node = to_node(target_pos)
    if not target_node in G.nodes:
        return
    act_plan = move_to_node_planner(env.saved_state, G, target_node)
    executor(env, act_plan)
