n = int(input())

results = list(map(int, input().split()))

winner_score = max(results)

for i in range(n):
    if results[i] == winner_score:
        winner_position = i
        break

max_vs_score = 0
for i in range(winner_position, n - 1):
    if results[i] % 10 == 5 and results[i + 1] < results[i] and results[i] > max_vs_score:
        max_vs_score = results[i]

if max_vs_score == 0:
    print(0)
else:
    count = 0
    for i in range(n):
        if results[i] > max_vs_score:
            count += 1

    print(count + 1)