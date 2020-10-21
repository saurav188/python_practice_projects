class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_unival_subtrees(root):
    if root.left is None and root.right is None:
        return 1
    result=count_unival_subtrees(root.left)+count_unival_subtrees(root.right)
    if root.left.val==root.right.val==root.val:
        result+=1
    return result

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1
#
# 5
#The 5 trees are:
#- The three single '1' leaf nodes. (+3)
#- The single '0' leaf node. (+1)
#- The [1, 1, 1] tree at the bottom. (+1)