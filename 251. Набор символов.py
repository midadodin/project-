from collections import defaultdict

s = input()
c = input()

c_dict = sorted(set(c))
min_len = len(s)
lines = []
count = 0

for length in range(len(c), len(s) + 1):
    for i in range(0, len(s) - length + 1):
        if i + length <= len(s):
            lines.append(s[i:i + length])

for line in lines:
    line_set = sorted(set(line))
    if line_set == c_dict:
        count += 1
        if len(line) < min_len:
            min_len = len(line)

if len(s) < len(c) or count == 0:
    min_len = 0

print(min_len)