import sys


def main():
    numbers = list(map(int, input().split()))
    n, k = numbers[0], numbers[1]

    numbers = list(map(int, input().split()))

    if n == 1:
        if numbers[0] == k:
            print(1)
        else:
            print(0)
        return

    left = 0
    right = 1
    currentSum = numbers[left] + numbers[right]
    count = 0
    i = 0

    while right <= n - 1:
        try:
            if currentSum == k:
                count += 1
                currentSum -= numbers[left]
                left += 1
                right += 1
                currentSum += numbers[right]
            elif currentSum > k:
                currentSum -= numbers[left]
                left += 1
                if left == right:
                    right += 1
                    currentSum += numbers[right]
            else:
                right += 1
                currentSum += numbers[right]
        except IndexError:
            pass

    for number in numbers:
        if number == k:
            count += 1

    print(count)


if __name__ == '__main__':
    main()