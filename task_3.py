import networkx as nx

# Завантаження графа
G = nx.read_adjlist("social_network.adjlist")

# Додавання ваг для ребер
weights = {
    ("Alice", "Bob"): 2, ("Bob", "Charlie"): 3, ("Charlie", "David"): 1,
    ("Alice", "Eve"): 4, ("Eve", "Frank"): 2, ("Frank", "Grace"): 5,
    ("Grace", "Helen"): 1, ("Helen", "David"): 3,
    ("Alice", "Ivy"): 6, ("Ivy", "Jack"): 2
}

for (u, v), weight in weights.items():
    if G.has_edge(u, v):
        G[u][v]['weight'] = weight

# Знаходження найкоротших шляхів за алгоритмом Дейкстри
print("\nНайкоротші шляхи між усіма вершинами графа:")
for source in G.nodes():
    for target in G.nodes():
        if source != target:
            try:
                path = nx.dijkstra_path(G, source, target)
                path_length = nx.dijkstra_path_length(G, source, target)
                print(f"{source} -> {target}: Шлях {path}, Довжина {path_length}")
            except nx.NetworkXNoPath:
                print(f"{source} -> {target}: Немає шляху")
