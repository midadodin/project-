from collections import deque

def room_area():
    n = int(input())

    cells = []
    for i in range(n):
        cells.append(input())

    line = list(map(int, input().split()))
    y_start, x_start = line[0], line[1]
    area = 1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    visited.add((x_start - 1, y_start - 1))

    queue = deque([(x_start - 1, y_start - 1)])
    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy        

            if 0 <= nx < n and 0 <= ny < n and cells[nx][ny] != '*' and (nx, ny) not in visited:
                visited.add((nx, ny))
                area += 1
                queue.append((nx, ny))

    print(area)

room_area()