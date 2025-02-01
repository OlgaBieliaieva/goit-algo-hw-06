import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (користувачів)
users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivy", "Jack"]
G.add_nodes_from(users)

# Додавання зв'язків (дружніх відносин) — для явної різниці між DFS та BFS збережено кількість зв'язків
friendships = [
    ("Alice", "Bob"), ("Bob", "Charlie"), ("Charlie", "David"),
    ("Alice", "Eve"), ("Eve", "Frank"), ("Frank", "Grace"),
    ("Grace", "Helen"), ("Helen", "David"),
    ("Alice", "Ivy"), ("Ivy", "Jack")
]
G.add_edges_from(friendships)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
plt.title("Соціальна мережа")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = dict(G.degree())

print("Основні характеристики графа:")
print(f"Кількість вершин (користувачів): {num_nodes}")
print(f"Кількість ребер (зв'язків): {num_edges}")
print("Ступені вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree}")

# Додатковий аналіз: найбільш центральний користувач
max_degree_user = max(degree_centrality, key=degree_centrality.get)
print(f"Користувач із найбільшою кількістю зв'язків: {max_degree_user} ({degree_centrality[max_degree_user]} зв'язків)")

nx.write_adjlist(G, "social_network.adjlist")