class Tree:
    def __init__(self,val=None):
        self.value = val

        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def is_empty(self):
        return (self.value == None)

    def insert(self, data):
        if self.is_empty():
            self.value = data
            self.right = Tree()
            self.left = Tree()
        elif data > self.value:
            self.right.insert(data)
            return
        elif data < self.value:
            self.left.insert(data)
            return
        else:
            return
        
    def inorder(self):
        if self.is_empty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()
        
line = list(map(int, input().split()))

tree = Tree(line[1])

for number in line:
    if number != 0:
        tree.insert(number)

inorder = tree.inorder()

for number in inorder:
    print(number)