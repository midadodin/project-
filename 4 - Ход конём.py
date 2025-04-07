def count_knight_paths(N, M):
    # Создаем таблицу для хранения количества способов добраться до каждой клетки
    dp = [[0] * M for _ in range(N)]
    
    # Инициализируем начальную позицию
    dp[0][0] = 1
    
    # Заполняем таблицу
    for i in range(N):
        for j in range(M):
            if i - 2 >= 0 and j - 1 >= 0:
                dp[i][j] += dp[i - 2][j - 1]
            if i - 1 >= 0 and j - 2 >= 0:
                dp[i][j] += dp[i - 1][j - 2]
    
    # Возвращаем количество способов добраться до правого нижнего угла
    return dp[N - 1][M - 1]

# Чтение входных данных
N, M = map(int, input().split())

# Вычисление и вывод результата
print(count_knight_paths(N, M))