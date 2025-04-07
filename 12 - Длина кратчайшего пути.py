from collections import deque

def shortest_path(n, graph, start, end):
    lines = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                lines[i].append(j)
    
    queue = deque([start - 1])
    visited = [False for _ in range(n)]
    visited[start - 1] = True
    distances = [-1 for _ in range(n)]
    distances[start - 1] = 0

    while queue:
        current = queue.popleft()
        for neighbor in lines[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    print(distances[end - 1])

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
line = list(map(int, input().split()))
start, end = line[0], line[1]

shortest_path(n, graph, start, end)
