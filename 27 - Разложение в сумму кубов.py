import sys

def main():
    n = int(input())
    dp = [i for i in range(n + 1)]

    cubes = [i**3 for i in range(1, n + 1)]

    current = 0
    cube = cubes[current]
    prev_cube = cubes[current]

    for i in range(2, n + 1):
        if i == cubes[current + 1]:
            dp[i] = 1
            current += 1
            prev_cube = cube
            cube = cubes[current]
            continue
        dp[i] = min(dp[i - cube], dp[i - prev_cube]) + 1

    print(dp[n])

if __name__ == '__main__':
    main()