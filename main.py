# Завдання 1
# Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

# Завдання 2
# Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
# Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

# Завдання 3
# Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
import networkx as nx
import matplotlib.pyplot as plt


def graph():
    G = nx.DiGraph()
    G.add_nodes_from(
        [
            "Router",
            "getAll",
            "postNewOne",
            "MainPage",
            "getDetailsByOne",
            "ThePost",
            "UserForm",
            "PostsPage",
        ]
    )
    G.add_edges_from(
        [
            ("Router", "getAll"),
            ("Router", "postNewOne"),
            ("Router", "getDetailsByOne"),
            ("getAll", "MainPage"),
            ("getAll", "PostsPage"),
            ("postNewOne", "UserForm"),
            ("getDetailsByOne", "ThePost"),
        ]
    )
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    print(f"Number of edges:{num_edges}\nNumber of nodes:{num_nodes}")

    nx.draw(G, with_labels=True)
    plt.show()


graph()
