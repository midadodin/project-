from math import sqrt

def f(x, a, b, c):
    return a if x < c else b

def result_function(x, y, n, a, b, c):
    return sqrt((f(x, a, b, c) - y) ** 2 / n)

n = int(input())
pairs = []
for _ in range(n):
    pairs.append(list(map(int, input().split())))

max_y = - 10 ** 9
min_y = 10 ** 9

y_values = []

x_sum = 0

for x, y in pairs:
    y_values.append(y)

    x_sum += x

y_values.sort()

y_mins = y_values[:n // 2]
y_maxs = y_values[n // 2:]
a = sum(y_maxs) / 2
b = sum(y_mins) / 2
c = x_sum / 4


print(a, b, c)