def bota_wins(n, m, numbers):
    # dp[i] - максимальная разница очков, которую может обеспечить Бока, начиная с позиции i
    dp = [-float('inf')] * (n + 1)
    dp[n] = 0  # Базовый случай: если нет чисел, то разница очков 0

    # Префиксные суммы для удобства подсчета
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + numbers[i]

    # Заполнение dp таблицы
    for i in range(n - 1, -1, -1):
        for k in range(1, m + 1):
            if i + k <= n:
                current_sum = prefix_sum[i + k] - prefix_sum[i]
                dp[i] = max(dp[i], current_sum - dp[i + k])
                print(current_sum, dp)

    return 1 if dp[0] > 0 else 0

# Чтение входных данных
import sys

data = input().split()

n = int(data[0])
m = int(data[1])
numbers = list(map(int, data[2:]))

# Вычисление и вывод результата
print(bota_wins(n, m, numbers))
