class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result

def serialize(root):
    if root.right==None and root.left==None:
        return str(root.val)+'##'
    if root.left==None:
        return str(root.val)+'#'+serialize(root.right)
    if root.right==None:
        return str(root.val)+serialize(root.left)+'#'
    return str(root.val)+serialize(root.left)+serialize(root.right)
def deserialize(data):
    def helper(data,start):
        if data[start]=='#':
            return [None,start]
        root=Node(data[start])
        [left_node,left_end]=helper(data,start+1)
        [right_node,right_end]=helper(data,left_end+1)
        root.left=left_node
        root.right=right_node

        return [root,right_end]
    temp=''
    for letter in data:
        if letter!=' ':
            temp+=letter
    [tree,end]=helper(temp,0)
    return tree

#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 132547
