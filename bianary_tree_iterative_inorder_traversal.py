class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def inorder(self):
        stack=[]
        current=self
        result=""
        while True:
            if current!=None:
                stack.append(current)
                current=current.left
            elif len(stack)>0:
                current=stack.pop()
                result+=current.val+"=>"
                current=current.right
            else:
                break
        return result
            

tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print(tree.inorder())

#     a
#    /  \
#   b    c
#  / \  / \
# d  e f   g