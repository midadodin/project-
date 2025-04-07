n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

prev_y = -1
length = 0

high_points = [[0, 0], points[0]]
for i in range(n - 1):
    x, y = points[i]
    if prev_y == -1:
        prev_y = y
        continue
    next_y = points[i + 1][1]
    prev_y = points[i - 1][1]

    if prev_y < y and y > next_y:
        high_points.append([x, y])


for i in range(1, len(high_points)):
    x1, y1 = high_points[i - 1]
    x2, y2 = high_points[i]
    length += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

for i in range(1, n):
    x1, y1 = points[i - 1]
    x2, y2 = points[i]
    length += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(length)