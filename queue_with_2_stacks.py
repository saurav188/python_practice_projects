class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def enqueue(self, val):
        self.stack1.append(val)
        temp=self.stack1
        self.stack2=[]
        for i in range(len(temp)-1,-1,-1):
            self.stack2.append(temp[i])

    def dequeue(self):
        self.stack1.pop(0)
        return self.stack2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3