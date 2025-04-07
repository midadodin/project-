n = int(input())

prev_number = int(input())
answer = 0

for _ in range(n - 1):
    number = int(input())
    answer +=   min(prev_number, number)
    prev_number = number

print(answer)