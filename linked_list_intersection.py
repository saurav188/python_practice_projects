def intersection(a, b):
    c=a
    while c:
        d=b
        while d:
            if c.val==d.val:
                return c
            d=d.next
        c=c.next
    return Node(None)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def prettyPrint(self):
        c = self
        while c:
            print(c.val,end=" ")
            c = c.next
            if c:
                print('->',end=' ')
            else:
                print()

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next
c = intersection(a, b)
a.prettyPrint()
b.prettyPrint()
c.prettyPrint()
# 3 4


#A = 1 -> 2 -> 3 -> 4
#B = 6 -> 3 -> 4
