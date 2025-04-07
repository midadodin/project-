class Tree:
    def __init__(self, val=None):
        self.value = val
        if self.value is not None:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def is_empty(self):
        return self.value is None

    def insert(self, data, depth=1):
        if self.is_empty():
            self.value = data
            self.left = Tree()
            self.right = Tree()
            return depth
        elif data < self.value:
            return self.left.insert(data, depth + 1)
        elif data > self.value:
            return self.right.insert(data, depth + 1)
        else:
            return -1  # Element is already in the tree

    def element_depth(self, element, current=1):
        if self.is_empty():
            return -1
        if self.value == element:
            return current
        elif element < self.value:
            return self.left.element_depth(element, current + 1)
        else:
            return self.right.element_depth(element, current + 1)

# Example usage:
numbers = list(map(int, input().split()))[:-1]
tree = Tree()
for i in numbers:
    depth = tree.insert(i)
    if depth != -1:
        print(depth, end=' ')