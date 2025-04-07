def main():
    numbers = list(map(int, input().split()))
    n, m = numbers[0], numbers[1]

    cells = [list(map(int, input().split())) for i in range(n)]
    prices = [[0 for j in range(m)] for i in range(n)]
    directions = [['' for j in range(m)] for i in range(n)]
    answer = []
    prices[0][0] = cells[0][0]
    for i in range(1, n):
        prices[i][0] = prices[i - 1][0] + cells[i][0]
        directions[i][0] = 'D'
    for i in range(1, m):
        prices[0][i] = prices[0][i - 1] + cells[0][i]
        directions[0][i] = 'R'

    for i in range(1, n):
        for j in range(1, m):
            down_price = prices[i - 1][j] + cells[i][j]
            right_price = prices[i][j - 1] + cells[i][j]
            prices[i][j] = max(down_price, right_price)
            if down_price > right_price:
                directions[i][j] = 'D'
            else:
                directions[i][j] = 'R'

    i, j = n - 1, m - 1
    answer = []
    while i > 0 or j > 0:
        answer.append(directions[i][j])
        if directions[i][j] == 'D':
            i -= 1
        else:
            j -= 1

    answer.reverse()

    print(prices[-1][-1])
    print(*answer)

main()