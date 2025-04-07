class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        print('ok')

    def back(self):
        if len(self.stack) > 0:
            print(self.stack[-1])
        else:
            print('error')

    def pop(self):
        if len(self.stack) > 0:
            print(self.stack.pop())
        else:
            print('error')

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack = []
        print('ok')

def main():
    stack = Stack()
    
    while True:
        line = input().split()
        command = line[0]

        if command == 'push':
            n = int(line[1])
            stack.push(n)
        elif command == 'pop':
            stack.pop()
        elif command == 'back':
            stack.back()
        elif command == 'size':
            stack.size()
        elif command == 'clear':
            stack.clear()
        elif command == 'exit':
            print('bye')
            return

main()