import sys

def main():
    dictionary = {}
    while True:
        line = sys.stdin.readline().split()

        if line == []:          
            break

        for word in line:
            dictionary[word] = 0

    print(len(dictionary))

if __name__ == '__main__':
    main()