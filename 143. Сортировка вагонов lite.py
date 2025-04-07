class Stack:
    def __init__(self) -> None:
        self.second_stack = []
        self.stop_stack = []
        
    def push(self, new_train):
        self.stop_stack.append(new_train)

    def last_train(self):
        if len(self.stop_stack) == 0:
            return False
        return self.stop_stack[-1]

    def clear_stop(self):
        print(self.stop_stack)
        if len(self.second_stack) == 0:
            if self.last_train() == 1:
                self.second_stack.append(self.stop_stack.pop())
            else: 
                return
        
        while self.last_train() == self.second_stack[-1] + 1:
            self.second_stack.append(self.stop_stack.pop())

    def check(self):
        return 'NO' if len(self.stop_stack) > 0 else 'YES'
    
def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    stack = Stack()
    for train in numbers:
        stack.push(train)
        stack.clear_stop()
    stack.clear_stop()
    print(stack.check())

main()