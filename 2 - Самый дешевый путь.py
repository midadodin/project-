def main():
    numbers = list(map(int, input().split()))
    n, m = numbers[0], numbers[1]

    cells = [list(map(int, input().split())) for i in range(n)]
    prices = [[float('inf') for j in range(m)] for i in range(n)]
    prices[0][0] = cells[0][0]

    for i in range(n):
        for j in range(m):
            steps = [(i + 1, j),
                     (i, j + 1)]
            for dx, dy in steps:
                if 0 <= dx < n and 0 <= dy < m:
                    prices[dx][dy] = min(prices[dx][dy], prices[i][j] + cells[dx][dy])

    print(prices[-1][-1])

main()