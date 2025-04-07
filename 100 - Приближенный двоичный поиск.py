def aprx_bin_search():
    n, k = list(map(int,  input().split()))
    array1 = list(map(int,  input().split()))
    array2 = list(map(int,  input().split()))

    for number_to_search in array2:
        left = 0
        right = n
        
        while abs(left - right) > 1:
            middle = (left + right) // 2
            if array1[middle] >= number_to_search:
                right = middle
            else:
                left = middle
        if right == n:
            print(array1[-1])
            continue
        if abs(array1[left] - number_to_search) == abs(array1[right] - number_to_search):
            print(min(array1[left], array1[right]))
        else:
            print(array1[left]) if abs(array1[left] - number_to_search) < abs(array1[right] - number_to_search) else print(array1[right])

aprx_bin_search()