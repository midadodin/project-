import string
gen1 = input()
gen2 = input()

bin1 = {}
bin2 = {}

letters = string.ascii_uppercase
for a in letters:
    for b in letters:
        bin1[f'{a}{b}'] = 0
        bin2[f'{a}{b}'] = 0

for i in range(len(gen1) - 1):
    bin1[f'{gen1[i]}{gen1[i + 1]}'] += 1

for i in range(len(gen2) - 1):
    bin2[f'{gen2[i]}{gen2[i + 1]}'] += 1

count = 0
for key in bin1.keys():
    if bin1[key] > 0 and bin2[key] > 0:
        count += bin1[key]

print(count)