#You are given a singly linked list and an integer k. Return the linked list, 
#removing the k-th last element from the list.

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def remove_kth_from_linked_list(head, k):
    temp=head
    remove_element=head
    remove_element_prev=None
    remove_element_next=head.next
    for i in range(k):
        temp=temp.next
    i=0
    while temp:
        if i==0:
            remove_element_prev=head
            i=1
        else:
            remove_element_prev=remove_element_prev.next
        remove_element=remove_element.next
        remove_element_next=remove_element_next.next
        temp=temp.next
    if remove_element_prev:
        remove_element_prev.next=remove_element_next
    else:
        head=head.next
    del remove_element
    return head

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 4, 5]

#1=>2=>3=>4=>5
#loop till k then make the first one the element(remove_element) to remove 
#then start from k till the end while increasing the remove_element
#at the end remove the remove element