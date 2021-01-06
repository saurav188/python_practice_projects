class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"


def create_tree(postorder):
    if len(postorder)==0:
        return None
    temp=Node(postorder[-1])
    if len(postorder)>1:
        temp.left=Node(postorder[0])
        temp.right=create_tree(postorder[1:len(postorder)-1])
    return temp

# 2 is the root node, with 1 as the left child and 3 as the right child
print(create_tree([1, 3, 2]))