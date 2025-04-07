from collections import deque

def short_path():
    line = list(map(int, input().split()))
    n, m = line[0], line[1]

    cells = []
    for i in range(n):
        cells.append(list(map(int, input().split())))

    queue = deque([(0, 0, 0)])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y, steps = queue.popleft()

        for dx, dy in directions:
            nx, ny = x, y

            while 0 <= nx + dx < n and 0 <= ny + dy < m and cells[nx + dx][ny + dy] != 1:
                nx += dx
                ny += dy

                if cells[nx][ny] == 2:
                    return steps + 1
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1
    
print(short_path())