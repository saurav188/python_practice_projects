import random

class node():
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
        self.parent=None
    def __str__(self):
        return str(self.val)
    def add(self,val):
        root=self
        if root.val==val:
            return
        elif val>root.val:
            if root.right==None:
                root.right=node(val)
                root.right.parent=root
                return val
            else:
                self.right.add(val)
        elif val<root.val:
            if root.left==None:
                root.left=node(val)
                root.left.parent=root
                return val
            else:
                self.left.add(val)
    def search(self,val):
        if val==None:
            return None
        elif self.val==val:
            return self
        elif val<self.val:
            if self.left:
                return self.left.search(val)
            else:
                return None
        elif val>self.val:
            if self.right:
                return self.right.search(val)
            else:
                return None
    def remove(self,val):
        node_to_remove=self.search(val)
        if not node_to_remove:
            #not in the tree
            return self
        parent=node_to_remove.parent
        if node_to_remove.left==None and node_to_remove.right==None:
            #both empty
            if node_to_remove==self:
                del self
                return None
            elif node_to_remove.val<parent.val:
                parent.left= None
            else:
                parent.right=None
            del node_to_remove

        elif node_to_remove.left==None:
            #left empty
            if node_to_remove== self:
                self=self.right
                del self.parent
                self.parent=None
            elif node_to_remove.val<parent.val:
                parent.left= node_to_remove.right
                node_to_remove.right.parent=parent
            else:
                parent.right=node_to_remove.right
                node_to_remove.right.parent=parent
            del node_to_remove

        elif node_to_remove.right==None:
            #right empty
            if node_to_remove== self:
                self=self.left
                del self.parent
                self.parent=None
            elif node_to_remove.val<parent.val:
                parent.left= node_to_remove.left
                node_to_remove.left.parent=parent
            else:
                parent.right=node_to_remove.left
                node_to_remove.left.parent=parent
            del node_to_remove

        else:
            #no empty child
            node_to_swap_with=self.leftmostnode(node_to_remove.right)
            node_to_remove.val=node_to_swap_with.val
            swap_parent=node_to_swap_with.parent
            #left empty
            if node_to_swap_with.val<swap_parent.val:\
                swap_parent.left= node_to_swap_with.right
            else:
                swap_parent.right=node_to_swap_with.right
            del node_to_swap_with
        return self
    def leftmostnode(self,node):
        if node.left==None:
            return node
        else:
            return self.leftmostnode(node.left) 
    def max(self):
        if self.right!= None:
            return self.right.max()
        return self.val
    def min(self):
        if self.left!= None:
            return self.left.min()
        return self.val
    def printInorder(self):
        if self!=None:
            if self.left!=None:
                self.left.printInorder()
            print(self.val,end=' => ')
            if self.right!=None:
                self.right.printInorder()
        return 
    def printDeorder(self):
        if self!=None:
            if self.right!=None:
                self.right.printDeorder()
            print(self.val,end=' => ')
            if self.left!=None:
                self.left.printDeorder()
        return
    def BFS(self,val):
        queue=[self]
        while len(queue)!=0:
            temp=queue.pop(0)
            if val==temp.val:
                return temp
            if temp.left!=None:
                queue.insert(0,temp.left)
            if temp.right!=None:
                queue.insert(0,temp.right)
        return 

n=node(5)
for i in range(10):
    n.add(random.randint(0,10))
n.printInorder()
print()
node_7=n.BFS(7)
temp=node_7
while temp:
    print(temp.val,end=' => ')
    temp=temp.parent 
