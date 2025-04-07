from collections import deque

def first_plus_one(number):
    if number[0] != '9':
        new_digit = int(number[0]) + 1
        return str(new_digit) + number[1:]
    else:
        return False

def last_plus_one(number):
    if number[-1] != '1':
        new_digit = int(number[-1]) - 1
        return number[:3] + str(new_digit)
    else:
        return False
    
def roll_right(number):
    return number[3] + number[:3]

def roll_left(number):
    return number[1:] + number[0]

def find_path():
    start = input()
    end = input()

    visited = [False for _ in range(10000)]
    visited[int(start)] = True

    distances = [-1 for _ in range(10000)]
    distances[int(start)] = 0
    
    predecessors = [None for _ in range(10000)]

    queue = deque([start])

    while queue and not visited[int(end)]:
        current = queue.popleft()

        next_numbers = [
            first_plus_one(current),
            last_plus_one(current),
            roll_right(current),
            roll_left(current)
        ]

        for number in next_numbers:
            if number and not visited[int(number)]:
                visited[int(number)] = True
                distances[int(number)] = distances[int(current)] + 1
                predecessors[int(number)] = current
                queue.append(number)
                if number == end:
                    break

    if distances[int(end)] != -1:
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors[int(current)]
        path.reverse()
    for i in range(len(path)):
        print(path[i])

find_path()
