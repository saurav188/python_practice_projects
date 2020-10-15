class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val)+'=>' if c.val else ""
            c = c.next
        return answer

def merge(lists):
    def merge_two(list1,list2):
        temp1=list1
        temp2=list2
        if temp1.val<temp2.val:
            merged=Node(list1.val)
            temp1=temp1.next
        else:
            merged=Node(list2.val)
            temp2=temp2.next
        temp_merged=merged
        while temp1 and temp2:
            if temp1.val<temp2.val:
                next_node=Node(temp1.val)
                temp1=temp1.next
            else:
                next_node=Node(temp2.val)
                temp2=temp2.next
            temp_merged.next=next_node
            temp_merged=temp_merged.next
        while temp1:
            temp_merged.next=Node(temp1.val)
            temp_merged=temp_merged.next
            temp1=temp1.next
        while temp2:
            temp_merged.next=Node(temp2.val)
            temp_merged=temp_merged.next
            temp2=temp2.next
        return merged

    temp=lists
    while len(temp)>1:
        temp[0]=merge_two(temp[0],temp[1])
        temp.pop(1)
    return temp[0]

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
c = Node(7, Node(8, Node(9)))
print(a)
print(b)
print(c)
print(merge([a, b,c]))