import sys


def main():
    numbers = list(map(int, input().split()))

    negativePair = [0, 0]
    positivePair = [0, 0]

    if len(numbers) == 2:
        print(min(numbers), max(numbers))
        return

    for number in numbers:
        if number > 0:
            if number >= positivePair[1]:
                positivePair[0] = positivePair[1]
                positivePair[1] = number
            elif number > positivePair[0]:
                positivePair[0] = number

        if number < 0:
            if number <= positivePair[1]:
                negativePair[0] = negativePair[1]
                negativePair[1] = number
            elif number < negativePair[0]:
                negativePair[0] = number

    if positivePair[0] * positivePair[1] == 0 and negativePair[0] * negativePair[1] == 0:
        print(negativePair[1], positivePair[1])
        return

    if positivePair[0] * positivePair[1] > negativePair[0] * negativePair[1]:
        print(positivePair[0], positivePair[1])
    else:
        print(negativePair[1], negativePair[0])

if __name__ == '__main__':
    main()