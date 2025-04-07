from collections import deque

class Goblins:
    def __init__(self):
        self.left_half = deque()
        self.right_half = deque()
        self.add_count = 0

    def new_operation(self, operation):
        operator = operation[0]

        if operator == '+':
            self.add_count += 1
            goblin_number = operation[1]
            
            if self.add_count % 2 != 0:
                if self.right_half:
                    self.left_half.append(self.right_half.popleft())
                    self.right_half.append(goblin_number)
                else:
                    self.left_half.append(goblin_number)
            else:
                self.right_half.append(goblin_number)
            
        elif operator == '*':
            self.add_count += 1
            goblin_number = operation[1]
            self.left_half.append(goblin_number)
        elif operator == '-':
            self.popleft()

    def popleft(self):
        if self.left_half:
            print(self.left_half.popleft())
            if self.right_half and self.add_count % 2 == 0:
                self.left_half.append(self.right_half.popleft())

        self.add_count -= 1

goblins = Goblins()

n = int(input())

for i in range(n):
    operation = input().split()
    goblins.new_operation(operation)
