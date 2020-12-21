class Node():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def most_freq_subtree_sum(root):
    def helper(root,dict):
        if root==None:
            return 0
        sum=root.val+helper(root.left,dict)+helper(root.right,dict)
        if dict.get(sum)==None:
            dict[sum]=1
        else:
            dict[sum]+=1
        return sum
    dict={}
    helper(root,dict)
    result=0
    for key in dict:
        if dict[key]>result:
            result=key
    return result

root = Node(3, Node(1), Node(-3))
print(most_freq_subtree_sum(root))
# 1