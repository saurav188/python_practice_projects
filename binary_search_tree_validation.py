class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    if root==None:
        return True

    if not is_bst(root.right) or not is_bst(root.left):
        return False

    if root.right is not None and root.right.key<root.key:
        return False
    if root.left is not None and root.left.key>root.key:
        return False
    
    return True

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
#1  4 6
