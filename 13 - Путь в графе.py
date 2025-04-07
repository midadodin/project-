from collections import deque

def bfs():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    numbers = list(map(int, input().split()))
    start, end = numbers[0], numbers[1]

    if start == end:
        print(0)
        return

    distances = [n for _ in range(n)]
    parents = [-1 for _ in range(n)]
    
    queue = deque([start - 1])
    distances[start - 1] = 0
    
    while queue:
        current = queue.popleft()
        for i in range(n):
            if matrix[current][i] == 1 and distances[current] + 1 < distances[i]:
                distances[i] = distances[current] + 1
                parents[i] = current
                queue.append(i)
 
    if distances[end - 1] == n:
        print(-1)
    else:
        path = []
        current = end - 1
        while current != -1:
            path.append(current + 1)
            current = parents[current]
        path.reverse()
        print(distances[end - 1])
        print(*path)

bfs()
