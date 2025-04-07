from collections import deque

def birthday():
    line = input().split()
    x1, y1 = ord(line[0][0]) - ord('a'), int(line[0][1]) - 1
    x2, y2 = ord(line[1][0]) - ord('a'), int(line[1][1]) - 1

    directions = [(-2, 1), (2, 1), (1, 2), (1, -2), 
                  (-2, -1), (2, -1), (-1, 2), (-1, -2)]

    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y, 0)])  # (x, y, distance)
        visited = set()
        visited.add((start_x, start_y))
        distances = [[-1 for _ in range(8)] for _ in range(8)]
        distances[start_x][start_y] = 0

        while queue:
            x, y, dist = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    distances[nx][ny] = dist + 1
                    queue.append((nx, ny, dist + 1))

        return distances

    distances1 = bfs(x1, y1)
    distances2 = bfs(x2, y2)

    min_path = float('inf')
    for i in range(8):
        for j in range(8):
            if distances1[i][j] != -1 and distances2[i][j] != -1 and distances2[i][j] == distances1[i][j]:
                min_path = min(min_path, distances1[i][j])
    if min_path == float('inf'):
        print(-1)
    else:
        print(min_path)

birthday()