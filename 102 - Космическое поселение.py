n, a, b, w, h = list(map(int, input().split()))

left = 0
right = max(w, h) // n
total_square = w * h

while left < right:
    middle = (left + right) // 2
    func = (a + 2 * middle) * (b + 2 * middle) * n
    if func >= total_square:
        right = middle
    else:
        left = middle + 1
print(left)