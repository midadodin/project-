def distance_squared(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def count_equal_sides(points):
    n = len(points)
    equal_sides_count = 0

    distances = {}
    for i in range(n):
        for j in range(i + 1, n):
            d = distance_squared(points[i], points[j])
            if d not in distances:
                distances[d] = set()
            distances[d].add((i, j))

    for i in range(n):
        for j in range(i + 1, n):
            d = distance_squared(points[i], points[j])
            for pair in distances[d]:
                if i in pair or j in pair:
                    continue
                equal_sides_count += 1

    return equal_sides_count

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    result = count_equal_sides(points)
    print(result)

if __name__ == "__main__":
    main()