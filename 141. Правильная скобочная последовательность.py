class Stack:
    
    def __init__(self) -> None:
        self.stack = []
        self.open_brackets = ['(', '[', '{']
        self.close_brackets = [')', ']', '}']
        self.dict_brackets = {'(':')', '[':']', '{':'}'}

    def push(self, new_bracket):
        if new_bracket in self.open_brackets:
            self.stack.append(new_bracket)
        elif len(self.stack) == 0:
            return False
        elif self.dict_brackets[self.stack.pop()] != new_bracket:
            return False
        return True
    
    def size(self):
        return len(self.stack)
    
    def show(self):
        print(self.stack)
    
def main():
    line = input()
    stack = Stack()
    for bracket in line:
        if not stack.push(bracket):
            print('no')
            return
    if stack.size() == 0:
        print('yes')
    else:
       
        print('no')

main()