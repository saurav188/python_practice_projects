class queue():
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def equeue(self,data):
        self.items.append(data)
    def dequeue(self): 
        if self.is_empty():
            return 'queue is empty.'
        self.items.remove(self.items[0])
    def iterate(self):
        if self.is_empty():
            print('no item')
            return
        for item in self.items:
            print(item)

queue=queue()
print(queue.dequeue())
print('*')
queue.equeue(1)
queue.equeue(2)
queue.equeue(2)
queue.equeue(2)
queue.iterate()
print('*')
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print('*')
queue.iterate()