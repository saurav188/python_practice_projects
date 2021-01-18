#Given a binary tree and an integer k, 
#filter the binary tree such that its 
#leaves don't contain the value k. Here are the rules:

#- If a leaf node has a value of k, remove it.
#- If a parent node has a value of k, 
#and all of its children are removed, remove it.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "("+ str(self.value)+":("+ str(self.left.__repr__())+","+ (self.right.__repr__())+"))"

def filter(tree, k):
    contains_leafnode=True
    while contains_leafnode:
        contains_leafnode=False
        is_leaf_node=tree.left==None and tree.right==None
        if is_leaf_node:
            if tree.value==k:
                return None
            else:
                return tree
        if tree.left!=None:
            temp=filter(tree.left, k)
            if temp==None:
                contains_leafnode=True
            tree.left=temp
        if tree.right!=None:
            temp=filter(tree.right,k)
            if temp==None:
                contains_leafnode=True
            tree.right=temp

    return tree

#     1
#    / \
#   1   1
#  /   /
# 2   1
n5 = Node(2)
n4 = Node(1)
n3 = Node(1, n4)
n2 = Node(1, n5)
n1 = Node(1, n2, n3)
print(n1)
print(filter(n1, 1))
#     1
#    /
#   1
#  /
# 2
# value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)
