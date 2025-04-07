n, m = list(map(int, input().split()))

buy = sorted(list(map(int, input().split())))
sell = sorted(list(map(int, input().split())))


sell_sum = 0

for i in range(min(n, m)):
    if sell[-1 - i] - buy[i] <= 0:
        break

    sell_sum += sell[-1 - i] - buy[i]

print(sell_sum)
