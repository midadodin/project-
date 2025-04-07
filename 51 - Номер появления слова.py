from collections import defaultdict
import sys

line = sys.stdin.read().strip().split()
answer = []

dict = defaultdict(int)
for word in line:
    dict[word] += 1
    answer.append(dict[word] - 1)

print(*answer)