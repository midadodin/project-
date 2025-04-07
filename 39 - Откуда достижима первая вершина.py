def dfs(n, m, connections):
    points = {i: [] for i in range(1, n + 1)}
    visited = [False] * (n + 1)
    
    for u, v in connections:
        points[v].append(u)
    
    def reverse_dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                for neighbor in points[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    reverse_dfs(1)
    
    good_points = [i for i in range(1, n + 1) if visited[i]]
    print(*good_points)

numbers = list(map(int, input().split()))
n, m = numbers[0], numbers[1]

connections = [list(map(int, input().split())) for _ in range(m)]

dfs(n, m, connections)