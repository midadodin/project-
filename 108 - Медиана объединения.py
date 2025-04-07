def create_new_array(line1, line2):
    point1 = point2 = 0
    new_array = []
    while point1 < len(line1) and point2 < len(line2):
        if line1[point1] < line2[point2]:
            new_array.append(line1[point1])
            point1 += 1
        else:
            new_array.append(line2[point2])
            point2 += 1
    while point1 < len(line1):
        new_array.append(line1[point1])
        point1 += 1
    while point2 < len(line2):
        new_array.append(line2[point2])
        point2 += 1
    return new_array


n, l = list(map(int, input().split()))

lines = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        new_array = create_new_array(lines[i], lines[j])
        print(new_array[l - 1])