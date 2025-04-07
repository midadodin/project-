n = int(input())

probability = []

for _ in range(n):
    a, b = list(map(int, input().split()))
    probability.append(a / 100 * b / 100)

probability_sum = sum(probability)

for i in range(n):
    print(probability[i] / probability_sum)