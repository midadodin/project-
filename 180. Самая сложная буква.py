n = int(input())
line = input()
times = list(map(int, input().split()))

prev_time = 0
max_time = 0

for i in range(n):
    delta = times[i] - prev_time
    if delta >= max_time:
        max_time = delta
        letter = line[i]
    prev_time = times[i]

print(letter)