from collections import defaultdict
import sys

##text = sys.stdin.readlines()
text = sys.stdin.readline()

dictionary = defaultdict(int)

for line in text:
    for symbol in line:
        if symbol not in ['\n', ' ']:
            dictionary[symbol] += 1

dictionary = sorted(dictionary.items(), key=lambda x: x[0])
max_count = 0
for symbol, count in dictionary:
    if count > max_count:
        max_count = count

for j in range(max_count, 0, -1):
    for i in range(len(dictionary)):
        print(' ', end='') if dictionary[i][1] < j else print('#', end='')
    if j > 0:
        print()

for symbol, count in dictionary:
    print(symbol, end='')