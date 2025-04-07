import sys


def main():
    numbers = list(map(int, input().split()))
    n, k, m = numbers[0], numbers[1], numbers[2]

    if k < m:
        print(0)
        return
    
    delta = k % m
    x = k // m
    answer = 0

    while n >= k:
       n = n - k + delta
       answer += x

    print(answer)

if __name__ == '__main__':
    main()