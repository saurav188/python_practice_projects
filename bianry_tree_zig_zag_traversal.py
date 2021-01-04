class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_order(tree):
    result=[]
    queue1=[tree]
    queue2=[]
    direction=1
    while len(queue1)>0:
        temp=queue1.pop()
        result.append(temp.value)
        if direction==1:
            if temp.left!=None:
                queue2.append(temp.left)
            if temp.right!=None:
                queue2.append(temp.right)
        else:
            if temp.right!=None:
                queue2.append(temp.right)
            if temp.left!=None:
                queue2.append(temp.left)
        if len(queue1)==0:
            queue1=queue2
            queue2=[]
            direction=-direction
    return result

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]