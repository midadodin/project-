import sys


def main():
    n = int(input())
    dict = {}
    for i in range(n):
        words = input().split()
        dict[words[0]] = words[1]
        dict[words[1]] = words[0]
    word = input()
    print(dict[word])
    

if __name__ == '__main__':
    main()