import sys

def cleanNumber(number):
    clean = ''
    for digit in number:
        if digit not in ['-', ')', '(']:
            clean += digit
    if clean[0] == '+':
        clean = clean[2:]
    elif clean[0] == '8':
        clean = clean[1:]
    else:
        clean = '495' + clean
    return clean

def main():
    n = 3
    number = cleanNumber(input())
    numbersToCheck = []

    for i in range(n):
        numbersToCheck.append(cleanNumber(input()))

    for numberToCheck in numbersToCheck:
        if numberToCheck == number:
            print('YES')
        else:
            print("NO")

    


if __name__ == '__main__':
    main()