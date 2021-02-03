class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

def find_subtree(s, t):
    if t==None:
        if s==None:
            return True
        else:
            return False
    queue_for_s=[s]
    queue_for_t=[t]
    is_subtree=True
    while len(queue_for_t)>0 and len(queue_for_s)>0:
        curent_s=queue_for_s.pop(0)
        curent_t=queue_for_t.pop(0)
        if curent_t.value!=curent_s.value:
            is_subtree=False
            break
        if curent_s.left!=None:
            queue_for_s.append(curent_s.left)
        if curent_s.right!=None:
            queue_for_s.append(curent_s.right)
        if curent_t.left!=None:
            queue_for_t.append(curent_s.left)
        if curent_t.right!=None:
            queue_for_t.append(curent_s.right)
    if is_subtree:
        return True
    else:
        return find_subtree(s,t.left) or find_subtree(s,t.right)


t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

print(find_subtree(s, t))
# True