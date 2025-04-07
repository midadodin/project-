def main():
    k = int(input())
    points = []
    y_min = x_min = 10 ** 9
    y_max = x_max = - 10 ** 9
    for _ in range(k):
        x, y = list(map(int, input().split()))
        x_max = max(x, x_max)
        y_max = max(y, y_max)
        x_min = min(x, x_min)
        y_min = min(y, y_min)

    print(x_min, y_min, x_max, y_max)                    


main()