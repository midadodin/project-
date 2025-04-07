a = int(input())
b = int(input())
n = int(input())
m = int(input())

min_first_line = 1 + (n - 1) * (a + 1)
min_second_line = 1 + (m - 1) * (b - 1)

max_first_line = (a + 1) * n + 1
max_second_line = (b + 1) * n + 1

if min_first_line > max_second_line or min_second_line > max_first_line:
    print(-1)
else:
    print(max(min_first_line, min_second_line), min(max_first_line, max_second_line))