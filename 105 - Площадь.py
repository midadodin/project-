n = int(input())
m = int(input())
t = int(input())

left = 0
right = min(n, m) // 2 - 1
square = n * m

while left < right:
    middle = (left + right) // 2

    pile_square = (n * middle + (m - 2 * middle) * middle) * 2
    if pile_square >= t:
        right = middle
    else:
        left = middle + 1

print(left) 