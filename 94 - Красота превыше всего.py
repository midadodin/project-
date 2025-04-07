from collections import defaultdict

def find_minimal_subarray_with_all_types(n, k, trees):
    count = defaultdict(int)
    unique_trees = 0

    left = 0

    min_length = n + 1
    min_left = 0
    min_right = 0

    for right in range(n):
        if count[trees[right]] == 0:
            unique_trees += 1
        count[trees[right]] += 1

        while unique_trees == k:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
                min_right = right

            count[trees[left]] -= 1
            if count[trees[left]] == 0:
                unique_trees -= 1
            left += 1

    return min_left + 1, min_right + 1
    
n, k = map(int, input().split())
trees = list(map(int, input().split()))
result = find_minimal_subarray_with_all_types(n, k, trees)
print(result[0], result[1])