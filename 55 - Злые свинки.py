n = int(input())

birds = {}

for i in range(n):
    coords = list(map(int, input().split()))
    x, y = coords[0], coords[1]
    birds[x] = y

print(len(birds))
"""
    try:
        birds[x].append(y)
    except KeyError:
        birds[x] = []
        birds[x].append(y)

for i in birds.items():
    key = i[0]
    birds[key] = sorted(birds[key], reverse=True)

birds = list(sorted(birds.items()))

for couples in birds:
    x = couples[0]
    y_coords = couples[1]
    """