class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def is_palindrome(node):
    last_node=node
    list_length=1
    while last_node.next is not None:
        last_node=last_node.next
        list_length+=1
    is_palindrome=True
    i=1
    while is_palindrome:
        if node.val!=last_node.val:
            return False
        if i>=list_length:
            is_palindrome=False
            continue
        node=node.next
        i+=1
        last_node=last_node.prev
        list_length-=1
    return True

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome(node))
# abba
# True
#O(n+n/2)