import sys


def main():
    numbers = list(map(int, input().split()))
    n, x, y = numbers[0], numbers[1], numbers[2]

    left = 0
    right = n * max(x, y)

    while left < right:
        mid = (right + left) // 2

        if (mid // x + mid // y) >= n - 1:
            right = mid
        else:
            left = mid + 1
        
    print(left + min(x, y))


if __name__ == '__main__':
    main()