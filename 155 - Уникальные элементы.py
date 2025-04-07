from collections import defaultdict

numbers_dict = defaultdict(int)

n = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    numbers_dict[number] += 1

answer = 0

for number in numbers:
    if numbers_dict[number] == 1:
        answer += 1

print(answer)