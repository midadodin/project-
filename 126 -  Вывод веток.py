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
        
    def get_root(self):
        return self.value
    
    def max_depth(self):
        if self.is_empty():
            return []
        else:
            left_depth = self.left.max_depth()
            right_depth = self.right.max_depth()
            return max(left_depth, right_depth) + 1
    
    def leafs(self):
        if self.is_empty():
            return []
        if (self.right.is_empty() and not self.left.is_empty()) or (not self.right.is_empty() and self.left.is_empty()):
            return self.left.leafs() + [self.value] + self.right.leafs()
        else:
            return self.left.leafs() + self.right.leafs()

numbers = list(map(int, input().split()))[:-1]
tree = Tree()
for i in numbers:
    tree.insert(i)

for leaf in tree.leafs():
    print(leaf)