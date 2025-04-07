from collections import defaultdict

diego_cards = defaultdict(int)

n = int(input())
numbers = list(map(int, input().split()))
for number in numbers:
    diego_cards[number] += 1
diego_cards = sorted(diego_cards)

k = int(input())
numbers = list(map(int, input().split()))

for card in numbers:
    left = 0
    right = n

    while left < right:
        middle = (left + right) // 2
        if diego_cards[middle] > card:
            right = middle
        else:
            left = middle + 1
    print(left)