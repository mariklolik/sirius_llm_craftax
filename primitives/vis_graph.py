import networkx as nx
from matplotlib import pyplot as plt


def visualize_grid_graph(G):
    """
    Функция для визуализации ориентированного графа на плоскости, где вершины
    уже представлены кортежами координат (y, x).

    Параметры:
    G -- ориентированный граф (networkx.DiGraph), где названия вершин - это кортежи (y, x).
    """
    # Извлекаем позиции вершин из их названий (кортежей координат)
    pos = {
        node: (node[1], -node[0]) for node in G.nodes()
    }  # Переворачиваем y для корректного отображения

    # Нарисуем граф с использованием заранее известных позиций узлов
    plt.figure(figsize=(8, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=500,
        font_size=10,
        font_weight="bold",
        edge_color="gray",
        arrows=True,
    )

    # Настройка отображения сетки
    plt.grid(True)
    plt.gca().set_aspect("equal", adjustable="box")  # Сохраняем пропорции 1:1
    plt.savefig("graph.png")
