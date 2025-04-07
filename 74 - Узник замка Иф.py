import sys


def main():
    a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
    options = [(a <= d) and (b <= e), (b <= e) and (a <= d), 
               (a <= e) and (c <= d), (c <= e) and (a <= d),
              (b <= e) and (c <= d), (c <= e) and (b <= d)]
    
    if any(options):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()