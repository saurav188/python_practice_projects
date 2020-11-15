import heapq

class minStack(object):
    def __init__(self):
        self.stack=[]
        self.min=[]
        heapq.heapify(self.min)

    def push(self, x):
        self.stack.append(x)
        heapq.heappush(self.min,x)

    def pop(self):
        if len(self.stack)==0:
            return None
        temp=self.stack.pop()
        temp2=heapq.heappop(self.min)
        if temp!=temp2:
            heapq.heappush(self.stack,temp2)
        
        return temp

    def top(self):
        if len(self.stack)==0:
            return None
        return self.stack[-1]

    def getMin(self):
        if len(self.stack)==0:
            return None
        temp=heapq.heappop(self.min)
        heapq.heappush(self.min,temp)

        return temp

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
#push(x)  --  Push element x onto stack.
#pop()    --  Removes the element on top of the stack.
#top()    --  Get the top element.
#getMin() --  Retrieve the minimum element in the stack.