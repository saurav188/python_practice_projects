from collections import deque

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            num = len(q)
            while num > 0:
                n = q.popleft()
                result += str(n.value)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                num = num - 1
            if len(q):
                result += "\n"

        return result

def fullBinaryTree(node):
    temp=node
    stack=[node]
    while len(stack):
        if temp.right==None and temp.left!=None:
            temp.value=temp.left.value
            del temp.left
            temp.left=None
            temp=stack.pop()
        elif temp.right!=None and temp.left==None:
            temp.value=temp.right.value
            del temp.right
            temp.right=None
            temp=stack.pop()
        elif temp.right==None and temp.left==None:
            temp=stack.pop()
        else:
            stack.append(temp.right) 
            stack.append(temp.left) 
            temp=stack.pop()
    return node

# Given this tree:
#     1
#    / \ 
#   2   3
#  /   / \
# 0   9   4

# We want a tree like:
#     1
#    / \ 
#   0   3
#      / \
#     9   4

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)
print(fullBinaryTree(tree))
# 1
# 03
# 94