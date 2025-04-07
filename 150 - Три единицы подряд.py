import sys
from itertools import product

"""
0 1 - 2
00 01 10 11 - 4
000 001 010 011 100 101 110 111 - 7
0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 - 13
5 - 24
6 - 44
7 - 81
8 - 149
"""

def main():
    n = int(input())
    combinations = [2, 4, 7]

    for i in range(3, n):
        combinations.append(combinations[i - 2] + combinations[i - 1] + combinations[i - 3])

    print(combinations[n - 1])


if __name__ == '__main__':
    main()