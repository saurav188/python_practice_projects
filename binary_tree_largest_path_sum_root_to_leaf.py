class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def largest_path_sum(tree):
    #checing for leaf node
    no_left_child=tree.left==None
    no_right_child=tree.right==None
    is_leaf_node=no_left_child and no_right_child
    if is_leaf_node:
        return [tree.value]
    if not no_left_child:
        left_node_largest_path=largest_path_sum(tree.left)
    else:
        left_node_largest_path=[]
    if not no_right_child:
        right_node_largest_path=largest_path_sum(tree.right)
    else:
        right_node_largest_path=[]
    if tree.value+sum(left_node_largest_path)>tree.value+sum(right_node_largest_path):
        return [tree.value]+left_node_largest_path
    else:
        return [tree.value]+right_node_largest_path

tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4
print(largest_path_sum(tree))
# [1, 3, 5]