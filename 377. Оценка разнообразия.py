from collections import defaultdict

n = int(input())
products = []
id_dict = defaultdict(int)
category_dict = defaultdict(list)

for _ in range(n):
    products.append(list(map(int, input().split())))
    id, category = products[-1]
    id_dict[id] = category

query = list(map(int, input().split()))

for i in range(n):
    category_dict[id_dict[query[i]]].append(i + 1)

min_diff = n
for category_query in category_dict.values():
    for i in range(len(category_query) - 1):
        min_diff = min(min_diff, category_query[i + 1] - category_query[i])

print(min_diff)
