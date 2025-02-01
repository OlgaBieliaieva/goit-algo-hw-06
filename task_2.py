import networkx as nx

# Load graph from file
G = nx.read_adjlist("social_network.adjlist")

# Функція DFS
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))
    return None

# Функція BFS
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
    return None

# Порівняння результатів для обох алгоритмів
start_node = "Alice"
goal_node = "David"

dfs_result = dfs_path(G, start_node, goal_node)
bfs_result = bfs_path(G, start_node, goal_node)

print("Результати пошуку шляхів:")
print(f"DFS шлях від {start_node} до {goal_node}: {dfs_result}")
print(f"BFS шлях від {start_node} до {goal_node}: {bfs_result}")

# Пояснення різниці в шляхах
print("\nПояснення:")
print("DFS обирає глибокий шлях у графі, поки не знайде ціль, тому може давати довші або незвичні маршрути.")
print("BFS обирає найкоротший шлях у термінах кількості ребер, тому часто надає оптимальний результат.")