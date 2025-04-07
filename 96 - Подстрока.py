import sys


def main():
    line = list(map(int, input().split()))
    n, k = line[0], line[1]
    line = input()

    left, right = 0, 0
    count = 0
    start = 0
    dict = {}
    for symbol in line:
        dict[symbol] = [0, 0]
    while right < n:
        if dict[line[right]][0] + 1 <= k:
            dict[line[right]][0] += 1
            dict[line[right]][1] = right
            right += 1
        else:
            if right - left > count:
                count = right - left
                start = left + 1
            dict[line[right]][0] -= 1
            left = dict[line[right]][1] + 1
            right = dict[line[right]][1] + 1
    print(count, start)


    

if __name__ == '__main__':
    main()