import sys


def main():
    n = int(input())
    tshirts = list(map(int, input().split()))
    tshirt = 0

    m = int(input())
    shorts = list(map(int, input().split()))
    short = 0
    minDelta = 10000000

    i, j = 0, 0
    while i <= n - 1 and j <= m - 1:
        delta = abs(tshirts[i] - shorts[j])
        if delta < minDelta:
            minDelta = delta
            tshirt = tshirts[i]
            short = shorts[j]
            if tshirts[i] < shorts[j]:
                i += 1
            else:
                j += 1
        else:
            if tshirts[i] < shorts[j]:
                i += 1
            else:
                j += 1

    print(tshirt, short)


if __name__ == '__main__':
    main()