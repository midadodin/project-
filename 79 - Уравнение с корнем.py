import sys

def main():
    a, b, c = int(input()), int(input()), int(input())
    if c < 0:
        print('NO SOLUTION')
        return
    if a == 0 and b == 0 and c == 0:
        print('MANY SOLUTIONS')
        return
    if c == 0 and a != 0:
        print(-b // a)
        return
    if a == 0 and b == c**2:
        print('MANY SOLUTIONS')
        return
    if a == 0 and b != c**2:
        print('NO SOLUTION')
        return
    if a == 0 and b == 0 and c != 0:
        print('NO SOLUTION')
        return
    
    print((c**2 - b) // a)

if __name__ == '__main__':
    main()