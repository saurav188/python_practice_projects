from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder):
    if len(inorder)==0:
        return None
    root_val=preorder[0]
    root=Node(root_val)
    if len(inorder)==1:
        return root
    root_i=inorder.index(root_val)
    left_vals=inorder[0:root_i]
    right_vals=inorder[root_i+1:len(inorder)]
    left_preorder=[]
    for val in preorder:
        if val in left_vals:
            left_preorder.append(val)
    right_preorder=[]
    for val in preorder:
        if val in right_vals:
            right_preorder.append(val)
    root.left=reconstruct(left_preorder,left_vals)
    root.right=reconstruct(right_preorder,right_vals)
    return root

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(tree)
# abcdefg

#    a
#   / \
#  b   c
# / \ / \
#d  e f  g