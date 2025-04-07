from collections import deque

def bfs(n, m, s, t):
    # Initialize the distances grid with -1 (unreachable)
    distances = [[-1 for _ in range(m)] for _ in range(n)]
    
    # Initialize the BFS queue with the feeder's position
    queue = deque([(s, t)])
    distances[s][t] = 0
    
    # Directions for knight's moves
    moves = [
        (2, -1), (2, 1), (-2, -1), (-2, 1),
        (1, -2), (1, 2), (-1, -2), (-1, 2)
    ]
    
    # Perform BFS
    while queue:
        x, y = queue.popleft()
        current_distance = distances[x][y]
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and distances[nx][ny] == -1:
                distances[nx][ny] = current_distance + 1
                queue.append((nx, ny))
    
    return distances

def main():
    # Read input
    inputNumbers = input().split()
    n, m, s, t, q = int(inputNumbers[0]), int(inputNumbers[1]), int(inputNumbers[2]) - 1, int(inputNumbers[3]) - 1, int(inputNumbers[4])
    
    fleas = []
    for _ in range(q):
        fleas.append(tuple(map(int, input().split())))
    
    # Perform BFS from the feeder
    distances = bfs(n, m, s, t)
    
    # Calculate the total minimum distance sum for all fleas
    total_distance = 0
    for fx, fy in fleas:
        fx -= 1
        fy -= 1
        if distances[fx][fy] == -1:
            print(-1)
            return
        total_distance += distances[fx][fy]
    
    print(total_distance)

if __name__ == '__main__':
    main()