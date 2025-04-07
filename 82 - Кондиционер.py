import sys


def main():
    numbers = list(map(int, input().split()))
    troom, tcond = numbers[0], numbers[1]
    option = input()

    if option == 'heat':
        if troom < tcond:
            print(tcond)
        else:
            print(troom)
    if option == 'freeze':
        if troom < tcond:
            print(troom)
        else:
            print(tcond)
    if option == 'auto':
        print(tcond)
    if option == 'fan':
        print(troom)

if __name__ == '__main__':
    main()