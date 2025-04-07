n, m, k = list(map(int, input().split()))

field = [[0 for i in range(m)] for j in range(n)]
coords = []
for i in range(k):
    coords.append(list(map(int, input().split())))

for x, y in coords:
    x -= 1
    y -= 1
    cells_to_raise = [[x + 1, y],
                      [x + 1, y + 1],
                      [x + 1, y - 1],
                      [x, y + 1],
                      [x, y - 1],
                      [x - 1, y],
                      [x - 1, y + 1],
                      [x - 1, y - 1],]
    for next_x, next_y in cells_to_raise:
        if 0 <= next_x <= n - 1 and 0 <= next_y <= m - 1:
            field[next_x][next_y] += 1
for x, y in coords:
    x -= 1
    y -= 1
    field[x][y] = '*'
for line in field:
    print(*line)