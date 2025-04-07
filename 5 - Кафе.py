def minimal_lunch_cost(N, costs):
    if N == 0:
        return (0, 0, 0, [])
    
    INF = float('inf')
    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    used_coupons = [[False] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(1, N + 1):
        cost = costs[i - 1]
        for j in range(i + 1):
            if dp[i - 1][j] != INF:
                new_coupons = j + (1 if cost > 100 else 0)
                if dp[i][new_coupons] > dp[i - 1][j] + cost:
                    dp[i][new_coupons] = dp[i - 1][j] + cost
                    used_coupons[i][new_coupons] = False
                if j > 0 and dp[i][j - 1] > dp[i - 1][j]:
                    dp[i][j - 1] = dp[i - 1][j]
                    used_coupons[i][j - 1] = True
    
    min_cost = INF
    remaining_coupons = -1
    for j in range(N + 1):
        if dp[N][j] < min_cost:
            min_cost = dp[N][j]
            remaining_coupons = j
    
    used_days = []
    current_coupons = remaining_coupons
    for i in range(N, 0, -1):
        if used_coupons[i][current_coupons]:
            used_days.append(i)
            current_coupons += 1
        else:
            current_coupons -= (1 if costs[i - 1] > 100 else 0)
    
    used_days.reverse()

    print(dp)
    return (min_cost, remaining_coupons, len(used_days), used_days)

# Чтение входных данных
N = int(input())
costs = []
for _ in range(N):
    costs.append(int(input()))

result = minimal_lunch_cost(N, costs)
print(result[0])
print(result[1], result[2])
for day in result[3]:
    print(day)