import sys

def main():
    line = list(map(int, input().split()))
    d = list(map(int, input().split()))
    n, r = line[0], line[1]
    left = 0
    right = 1
    answer = 0

    while left < len(d) and right < len(d):
        if d[right] - d[left] <= r:
            right += 1
        else:
            answer += len(d) - right
            left += 1
            
    print(answer)

if __name__ == '__main__':
    main()