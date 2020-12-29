class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    def list_cousins(self, tree, val):
        cousins=[]
        queue1=[tree]
        queue2=[]
        this_level=False
        while len(queue1)>0:
            temp=queue1.pop(0)
            if temp.left!=None:
                queue2.append(temp.left)
            if temp.right!=None:
                queue2.append(temp.right)
            if len(queue1)==0:
                if val in [each.value for each in queue2]:
                    cousins=[each.value for each in queue2]
                    cousins.remove(val)
                    break
                queue1=queue2
                queue2=[]
        return cousins

#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution().list_cousins(root, 4))
# [4, 6]