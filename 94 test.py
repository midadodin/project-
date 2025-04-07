from collections import defaultdict

N, K = list(map(int,input().split()))
trees = list(map(int,input().split()))
left = 0
now_amount = 0
number_of_numbers = defaultdict(int)
left_granitsa = 0
right_granitsa = 0
length = N

for right in range (N):
    if number_of_numbers[trees[right]] == 0:
        now_amount += 1
    number_of_numbers[trees[right]] += 1

    while now_amount == K:
        if length > (right - left + 1):
            length = right - left + 1
            left_granitsa = left + 1
            right_granitsa = right + 1

        number_of_numbers[trees[left]] -= 1
        if number_of_numbers[trees[left]] == 0:
            now_amount -= 1
        left += 1

print (left_granitsa, right_granitsa)