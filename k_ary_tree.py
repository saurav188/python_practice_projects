class Node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def is_symmetric(root):
    if len(root.children)%2!=0:
        return False
    elif len(root.children)==0:
        return True
    i=0
    j=len(root.children)-1
    queue1=[root.children[i]]
    queue2=[root.children[j]]
    while i<j:
        temp1=[child for child in queue1[0].children]
        temp2=[child for child in queue2[0].children]
        if queue1.pop(0).value!=queue2.pop(0).value:
            return False
        queue1+=temp1
        queue2+=temp2
        i+=1
        j-=1
    return True

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
#        4
#     /     \
#    3        3
#  / | \    / | \
#9   4  1  1  4  9
print(is_symmetric(tree))
# True