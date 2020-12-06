class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_level_order(root):
    queue=[root]
    while len(queue)!=0:
        node=queue.pop()
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)
        print(node.val,end='')

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5