#Given a linked list of integers, remove all consecutive nodes that sum up to 0.

#Example:
#Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
#Output: 10

class Node():
    def __init__(self, value,next=None):
        self.value = value
        self.next = next

def removeConsecutiveSumTo0(node):
    first_node=node
    previous_node=node
    while node:
        current_node=node
        sum_of_nodes=0
        while current_node:
            sum_of_nodes+=current_node.value
            if sum_of_nodes==0:
                temp=previous_node.next
                previous_node.next=current_node.next
                node=first_node
                current_node.next=None
                while temp:
                    next_temp=temp.next
                    del temp
                    temp=next_temp
                current_node=node
            current_node=current_node.next
        previous_node=node
        node=node.next
    return first_node


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
    if node.next:
        print(node.value,end=' -> ')
    else:
        print(node.value)
    node = node.next
# 10

#10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
#check node by node
#first check
#10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4  nothing changes because 10+5..is never=0
#10 -> 4 -> -4   bacause 5-3-3+1=0 they are removed
#start from the biginning
#10 -> 4 -> -4
#10
#continue until all the nodes are checked