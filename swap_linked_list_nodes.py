#Given a linked list, swap the position of 
#the 1st and 2nd node, then swap 
#the position of the 3rd and 4th node etc.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"

def swap_every_two(linked_list):
    temp1=linked_list
    temp2=linked_list.next
    while temp1!=None and temp2!=None:
        temp=temp1.value
        temp1.value=temp2.value
        temp2.value=temp
        temp1=temp2.next
        temp2=temp1.next
    return linked_list

linked_list = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(linked_list)
print(swap_every_two(linked_list))
# 2, (1, (4, (3, (5, (None)))))
# 1=>2=>3>4=>5