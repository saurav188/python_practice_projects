from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        queue2=[]
        queue1=[self]
        result=""
        while len(queue1)>0:
            root=queue1.pop(0)
            result+=root.val
            if root.left!=None:
                queue2.append(root.left)
            if root.right!=None:
                queue2.append(root.right)
            if len(queue1)==0:
                queue1=queue2
                queue2=[]
                result+="\n"
        return result

tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print(tree)
# a
# bc
# defg