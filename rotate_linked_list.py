class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current = self
        ret = ''
        while current!=None:
            ret += str(current.value)
            current = current.next
        return ret

def rotate_list(list, k):
    for i in range(k):
        temp=list
        while temp.next!=None:
            if temp.next.next==None:
                start=temp.next
                temp.next=None
                break
            temp=temp.next
        start.next=list
        list=start
    return list

# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 4))
# 3412