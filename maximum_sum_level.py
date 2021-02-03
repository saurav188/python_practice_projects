class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def tree_level_max_sum(root):
    stack=[root]
    level=[]
    sums={}
    level_no=0
    sum=0
    max_level=0
    while len(stack)>0:
        temp=stack.pop()
        sum+=temp.value
        if temp.right!=None:
            level.append(temp.right)
        if temp.left!=None:
            level.append(temp.left)
        if len(stack)==0:
            stack=level
            sums[level_no]=sum
            if sum>=sums[max_level]:
                max_level=level_no
            sum=0
            level_no+=1
            level=[]
    return max_level

n3 = Node(4, Node(3), Node(2))
n2 = Node(5, Node(4), Node(-1))
n1 = Node(1, n2, n3)

"""
    1          Level 0 - Sum: 1
   / \
  4   5        Level 1 - Sum: 9 
 / \ / \
3  2 4 -1      Level 2 - Sum: 8

"""

print(tree_level_max_sum(n1))
# Should print 1 as level 1 has the highest level sum