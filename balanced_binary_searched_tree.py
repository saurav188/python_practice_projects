from collections import deque

class Node:
    def __init__(self, value, left=None, right=None,root=None):
        self.value = value
        self.left = left
        self.right = right
        if root is None:
            self.root=self
        else:
            self.root=root
    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer
    def get_height(self=None):
        if self==None:
            return 0
        elif self.right==None and self.left== None:
            return 1
        elif self.right==None:
            return self.left.get_height()+1
        elif self.left==None:
            return self.right.get_height()+1

        return max(self.right.get_height(),self.left.get_height())+1    
    def right_rotation(self,root):#increses height of right side by 1
        new_root=self.left
        temp=new_root.right

        new_root.right=self
        self.left=temp

        return new_root
    def left_rotation(self,root):#increses height of left side by 1
        new_root=self.right
        temp=new_root.left

        new_root.left=self
        self.right=temp
        return new_root     
    def printInorder(self):
        if self!=None:
            if self.left!=None:
                self.left.printInorder()
            print(self.value,end=' => ')
            if self.right!=None:
                self.right.printInorder()
        return 
    def add_node(self,val,root):
        if val>self.value:
            if self.right is None:
                self.right=Node(value=val,root=root)
            else:
                self.right=self.right.add_node(val,root=root)
        elif val<self.value:
            if self.left is None:
                self.left=Node(value=val,root=root)
            else:
                self.left=self.left.add_node(val,root=root)
        self=self.balance(val,root=self)
        return self
    def balance(self,val,root):
        #finding height difference
        if root.right!= None and root.left!= None:
            dif_height=root.right.get_height()-root.left.get_height()
        elif root.right==None:
            dif_height=0-root.left.get_height()
        elif root.left==None:
            dif_height=root.right.get_height()

        #all cases for balancing
        if 1>=dif_height>=-1:
            return root
        #case right right
        elif dif_height>1 and val>root.right.value:
            return root.left_rotation(root)
        #case left left
        elif dif_height<-1 and val<root.left.value:
            return root.right_rotation(root)
        #case right left
        elif dif_height>1 and val<root.right.value:
            root.right=root.right.right_rotation(root.right)
            return root.left_rotation(root)
        #case left right
        elif dif_height<-1 and val>root.left.value:
            root.left=root.left.left_rotation(root.left)
            return root.right_rotation(root)

def createBalancedBST(nums):
    node=Node(nums[0])
    for n in range(1,len(nums)):
        node=node.add_node(nums[n],root=node)
    return node

tree=createBalancedBST([1, 2,3,4,5,6, 7])
print(tree)
# 4261357
#     4
#   /   \
#  2     6
# / \   / \
#1   3 5   7