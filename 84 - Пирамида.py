n = int(input())
sizes = {}

for i in range(n):
    numbers = list(map(int, input().split()))
    if numbers[0] not in sizes:
        sizes[numbers[0]] = [numbers[1]]
    else:
        sizes[numbers[0]].append(numbers[1])

max_height = 0
for key in sizes.keys():
    max_height += max(sizes[key])

print(max_height)