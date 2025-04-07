n = int(input())
key_strength = list(map(int, input().split()))
k = int(input())
key_input = list(map(int, input().split()))

for i in range(k):
    key_strength[key_input[i] - 1] -= 1

for key in key_strength:
    print('YES') if key < 0 else print('NO')
