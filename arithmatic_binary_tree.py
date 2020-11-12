class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    if root.left==None and root.right==None:
        if root.val in ['+','-','*','/']:
            return 'invalid input.leaf node must be a number'
        return str(root.val)
    if root.val not in ['+','-','*','/']:
        return 'invalid input.root node must be an operation'
    expression=evaluate(root.left)+root.val+evaluate(root.right)
    for i in range(len(expression)):
        if expression[i] in ['+','-','*','/']:
            operation=expression[i]
            operation_index=i
            break
    if operation=='+':
        result=int(expression[:operation_index])+int(expression[operation_index+1:])
    elif operation=='-':
        result=int(expression[:operation_index])-int(expression[operation_index+1:])
    elif operation=='*':
        result=int(expression[:operation_index])*int(expression[operation_index+1:])
    elif operation=='/':
        result=int(expression[:operation_index])/int(expression[operation_index+1:])
    return str(result)

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
#    *
#   / \
#  +    +
# / \  / \
#3  2  4  5
#(3 + 2) * (4 + 5)
# 45
