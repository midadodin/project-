n, k = list(map(int, input().split()))
stops = list(map(int, input().split()))
coords = list(map(int, input().split()))

for coord in coords:
    left = 0
    right = n - 1

    while left < right:
        middle = (left + right) // 2
        if stops[middle] < coord:
            left = middle + 1
        else:
            right = middle

    if left > 0 and abs(stops[left - 1] - coord) <= abs(stops[left] - coord):
        print(left)
    else:
        print(left + 1)
