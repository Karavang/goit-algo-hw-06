# Завдання 1
# Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

# Завдання 2
# Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
# Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

# Завдання 3
# Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def dfs_manual(graph, start):
    visited = set()
    edges = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                edges.append((node, neighbor))
                dfs(neighbor)

    dfs(start)
    return edges


def bfs_manual(graph, start):
    visited = set()
    queue = deque([start])
    edges = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    edges.append((node, neighbor))
                    queue.append(neighbor)

    return edges


def firstAndSecond():
    data = {
        "Router": ["getAll", "postNewOne", "getDetailsByOne"],
        "getAll": ["MainPage", "PostsPage"],
        "postNewOne": ["UserForm"],
        "getDetailsByOne": ["ThePost"],
        "MainPage": [],
        "PostsPage": [],
        "UserForm": [],
        "ThePost": [],
    }
    G = nx.DiGraph(data)
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    print(f"Number of edges:{num_edges}\nNumber of nodes:{num_nodes}")
    nx.draw(G, with_labels=True)

    dfs_tree = dfs_manual(data, "Router")
    print(list(dfs_tree))
    bfs_tree = bfs_manual(data, "Router")
    print(list(bfs_tree))
    plt.show()


def dijkstra_manual(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    paths[start] = [start]
    unvisited = set(graph.keys())
    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        if distances[current] == float("infinity"):
            break
        unvisited.remove(current)
        for neighbor, weight in graph[current].items():
            if neighbor in unvisited:
                new_distance = distances[current] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    paths[neighbor] = paths[current] + [neighbor]

    return distances, paths


def sigizmund():
    data = {
        "Kyiv": {
            "Donetsk": 650,
            "Kharkiv": 480,
            "Lviv": 540,
            "Poltava": 330,
            "Frankivsk": 480,
            "Zaporizhzhia": 520,
            "Dnepr": 480,
        },
        "Donetsk": {
            "Kyiv": 650,
            "Kharkiv": 300,
            "Lviv": 1100,
            "Poltava": 380,
            "Frankivsk": 980,
            "Zaporizhzhia": 200,
            "Dnepr": 230,
        },
        "Kharkiv": {
            "Kyiv": 480,
            "Donetsk": 300,
            "Lviv": 800,
            "Poltava": 150,
            "Frankivsk": 750,
            "Zaporizhzhia": 350,
            "Dnepr": 220,
        },
        "Lviv": {
            "Kyiv": 540,
            "Donetsk": 1100,
            "Kharkiv": 800,
            "Poltava": 650,
            "Frankivsk": 140,
            "Zaporizhzhia": 900,
            "Dnepr": 750,
        },
        "Poltava": {
            "Kyiv": 330,
            "Donetsk": 380,
            "Kharkiv": 150,
            "Lviv": 650,
            "Frankivsk": 600,
            "Zaporizhzhia": 280,
            "Dnepr": 150,
        },
        "Frankivsk": {
            "Kyiv": 480,
            "Donetsk": 980,
            "Kharkiv": 750,
            "Lviv": 140,
            "Poltava": 600,
            "Zaporizhzhia": 850,
            "Dnepr": 680,
        },
        "Zaporizhzhia": {
            "Kyiv": 520,
            "Donetsk": 200,
            "Kharkiv": 350,
            "Lviv": 900,
            "Poltava": 280,
            "Frankivsk": 850,
            "Dnepr": 80,
        },
        "Dnepr": {
            "Kyiv": 480,
            "Donetsk": 230,
            "Kharkiv": 220,
            "Lviv": 750,
            "Poltava": 150,
            "Frankivsk": 680,
            "Zaporizhzhia": 80,
        },
    }

    distances, paths = dijkstra_manual(data, "Kyiv")

    for city, distance in distances.items():
        if city != "Kyiv":
            print(
                f"Найкоротший шлях до {city}: {' -> '.join(paths[city])} ({distance} км)"
            )

    G = nx.Graph()
    for city1, neighbors in data.items():
        for city2, weight in neighbors.items():
            G.add_edge(city1, city2, weight=weight)

    pos = {
        "Kyiv": (30.5, 50.4),
        "Kharkiv": (36.2, 49.9),
        "Donetsk": (37.8, 48.0),
        "Dnepr": (35.0, 48.5),
        "Zaporizhzhia": (35.2, 47.8),
        "Poltava": (34.5, 49.6),
        "Lviv": (24.0, 49.8),
        "Frankivsk": (24.7, 48.9),
    }

    plt.figure(figsize=(15, 10))
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=2000, alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    nx.draw_networkx_edges(G, pos, alpha=0.6, width=1, edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)

    colors = ["red", "blue", "green", "orange", "purple", "brown", "pink"]
    for i, (city, path) in enumerate(paths.items()):
        if city != "Kyiv" and len(path) > 1:
            path_edges = [(path[j], path[j + 1]) for j in range(len(path) - 1)]
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=path_edges,
                edge_color=colors[i % len(colors)],
                width=3,
                alpha=0.7,
            )

    plt.title("Граф міст України з найкоротшими шляхами до Київа", fontsize=16)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    cities = [city for city in distances.keys() if city != "Kyiv"]
    distances_values = [distances[city] for city in cities]

    bars = plt.bar(cities, distances_values, color="skyblue", alpha=0.7)
    plt.title("Найкоротші шляхи від Київа до інших міст", fontsize=14)
    plt.xlabel("Місто", fontsize=12)
    plt.ylabel("Відстань (км)", fontsize=12)
    plt.xticks(rotation=45)

    for bar, distance in zip(bars, distances_values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 10,
            f"{distance}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    plt.tight_layout()
    plt.show()


firstAndSecond()
sigizmund()
