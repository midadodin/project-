from collections import defaultdict

n = int(input())
numbers = list(map(int, input().split()))

numbers_dict = defaultdict(int)

for number in numbers:
    numbers_dict[number] += 1

max_count = 0
max_number = 0

for number in numbers:
    if numbers_dict[number] > max_count:
        max_count = numbers_dict[number]
        max_number = number
    if numbers_dict[number] == max_count and number > max_number:
        max_number = number

print(max_number)