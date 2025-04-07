n = int(input())
count = 0
truth = {}

for i in range(n):
    truth[f'{i} {n - i - 1}'] = 0

for i in range(n):
    numbers = input()
    a, b = list(map(int, numbers.split()))
    if a + b == n - 1 and a >= 0 and b >= 0 and truth[f'{a} {b}'] == 0:
        count += 1
        truth[f'{a} {b}'] = 1

print(count)