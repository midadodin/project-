from collections import deque

numbers = list(map(int, input().split()))
k, n = numbers[0], numbers[1]

free_ends = {i: True for i in range(1, k + 1)}

arrive = []
depart = []

