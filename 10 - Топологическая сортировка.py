from collections import deque, defaultdict

def topological_sort_kahn(N, edges):
    in_degree = [0] * (N + 1)
    graph = defaultdict(list)

    # Построение графа и подсчет степеней входа
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Очередь для вершин с нулевой степенью входа
    queue = deque([i for i in range(1, N + 1) if in_degree[i] == 0])
    topo_sort = []

    while queue:
        node = queue.popleft()
        topo_sort.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Если количество вершин в топологической сортировке меньше N, значит, есть цикл
    if len(topo_sort) != N:
        return -1
    return topo_sort

# Чтение входных данных
N, M = map(int, input().split())
edges = []

for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

# Получение результата и вывод
result = topological_sort_kahn(N, edges)
if result == -1:
    print(result)
else:
    print(" ".join(map(str, result)))