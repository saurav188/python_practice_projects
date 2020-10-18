class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    return self.val

def deepest(node):
    if node.right==None and node.left==None:
        return [node.val,1]
    elif node.right==None:
        left= deepest(node.left)
        left[1]+=1
        return left
    elif node.left==None:
        right= deepest(node.right)
        right[1]+=1
        return right
    else:
        right=deepest(node.right)
        right[1]+=1
        left=deepest(node.left)
        left[1]+=1
        if right[1]>left[1]:
            return right
        else:
            return left

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)