import sys


def main():
    numbers = list(map(int, input().split()))
    w, h, n = numbers[0], numbers[1], numbers[2]

    left = 0
    right = n * max(w, h)
    c = 0
    
    while left < right:
        mid = (right + left) // 2

        if (mid // w) * (mid // h) >= n:
            right = mid
        else:
            left = mid + 1

    print(left)

if __name__ == '__main__':
    main()