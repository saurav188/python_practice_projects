class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        result = str(self.value)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result

def generate_bst(n):
    def helper(start,end):
        result=[]
        if start>end:
            result.append(None)
            return result
        for i in range(start,end+1):
            right=helper(i+1,end)
            left=helper(start,i-1)
            for each_left in left:
                for each_right in right:
                    node=Node(i)
                    node.right=each_right
                    node.left=each_left
                    result.append(node)
        return result
    return helper(1,n)
for tree in generate_bst(3):
    print(tree)

# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1