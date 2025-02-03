import networkx as nx
import heapq

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

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Відстані від стартової вершини до всіх інших (початково нескінченність)
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    # Черга пріоритетів (відстань, вузол)
    priority_queue = [(0, start)]
    # Відстеження попередників для відновлення шляху
    predecessors = {node: None for node in graph.nodes}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Пропускаємо обробку, якщо знайдено коротший шлях
        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            # Якщо знайшли коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

# Відновлення шляху
def get_path(predecessors, target):
    path = []
    current = target
    while current:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path if len(path) > 1 else None

# Знаходження найкоротших шляхів між усіма парами вершин
print("\nНайкоротші шляхи між усіма вершинами графа:")
for source in G.nodes:
    for target in G.nodes:
        if source != target:
            distances, predecessors = dijkstra(G, source)
            path = get_path(predecessors, target)
            if path:
                print(f"{source} -> {target}: Шлях {path}, Довжина {distances[target]}")
            else:
                print(f"{source} -> {target}: Немає шляху")