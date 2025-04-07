from collections import deque

def dfs(n, m, connections):
    points = {i: [] for i in range(1, n + 1)}
    visited = [False] * (n + 1)
    for connect in connections:
        u, v = connect
        points[u].append(v)
        points[v].append(u)
    
    queue = deque([1])
    visited[1] = True

    while queue:
        node = queue.pop()
        for neighbor in points[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    good_points = [i for i, v in enumerate(visited) if v and i != 0]

    print(len(good_points))
    print(*good_points)


numbers = list(map(int, input().split()))
n, m = numbers[0], numbers[1]

connections = [list(map(int, input().split())) for _ in range(m)]

dfs(n, m, connections)