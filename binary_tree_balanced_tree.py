class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_height(root):
    if root==None:
        return 0
    return max(get_height(root.left),get_height(root.right))+1

def is_height_balanced(tree):
    if abs(get_height(tree.right)-get_height(tree.left))>1:
        return False
    return True

#     1
#    / \
#   2   3
#  /
# 4  
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    / 
#   2   
#  /
# 4  
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False