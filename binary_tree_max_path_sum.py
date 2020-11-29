class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPathSum(root):
    sum=0
    queue=[]
    if sum+root.val>sum:
        sum+=root.val
        if root.left!=None and root.left.val+sum>sum:
            sum+=root.left.val
            temp=root.left
            if temp.left!=None:
                queue.append(temp.left)
            if temp.right!=None:
                queue.append(temp.right)
        if root.right!=None and root.right.val+sum>sum:
            sum+=root.right.val
            temp=root.right
            if temp.left!=None:
                queue.append(temp.left)
            if temp.right!=None:
                queue.append(temp.right)
    while len(queue)>0:
        if len(queue)>1:
            temp1=queue.pop(0)
            temp2=queue.pop(0)
            if sum+temp1.val>sum and sum+temp1.val>sum+temp2.val:
                sum+=temp1.val
                if temp1.left!=None:
                    queue.append(temp1.left)
                if temp1.right!=None:
                    queue.append(temp1.right)
            elif sum+temp2.val>sum and sum+temp2.val>sum+temp1.val:
                sum+=temp2.val
                if temp2.left!=None:
                    queue.append(temp2.left)
                if temp2.right!=None:
                    queue.append(temp2.right)
            continue
        temp=queue.pop(0)
        if sum+temp.val>sum:
            sum+=temp.val
            if temp.left!=None:
                queue.append(temp.left)
            if temp.right!=None:
                queue.append(temp.right)
    return sum
# (* denotes the max parth)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(maxPathSum(root))
# 42