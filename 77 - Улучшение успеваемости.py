import sys

def main():
    a, b, c = int(input()), int(input()), int(input())
    def average_score(fives):
        return (a * 2 + b * 3 + c * 4 + fives * 5) / (a + b + c + fives)
    
    left = 0
    right = a + b + c
    while left < right:
        mid = (left + right) // 2
        if round(average_score(mid)) >= 4:
            right = mid
        else:
            left = mid + 1
    
    print(left) 

if __name__ == '__main__':
    main()