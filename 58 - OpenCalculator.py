keys = input().split()

number = input()

all_keys = {f'{i}':False for i in range(10)}

for digit in number:
    if digit not in keys:
        all_keys[digit] = True

count = 0
for key in all_keys.keys():
    if all_keys[key]:
        count += 1

print(count)