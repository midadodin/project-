from collections import defaultdict
import sys

line = sys.stdin.read().strip().split()

dict = defaultdict(int)
for word in line:
    dict[word] += 1

dict = sorted(dict.items())
max_count = 0
max_word = ''

for word, count in dict:
    if count > max_count:
        max_word = word
        max_count = count

print(max_word)