class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.operands = ['+', '-', '*']

    def push(self, x):
        if x in self.operands:
            a, b = self.stack.pop(), self.stack.pop()
            if x == '+':
                result = a + b
            elif x == '-':
                result = b - a
            else:
                result = a * b
            self.stack.append(result)

        else:
            self.stack.append(int(x))

    def result(self):
        return self.stack.pop()

def main():
    line  = input().split()
    stack = Stack()
    for x in line:
        stack.push(x)

    print(stack.result())

main()