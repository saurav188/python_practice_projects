class stack():
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if stack.is_empty():
            return 'no item in stack'
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

stack=stack()
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.pop())
print(stack.pop())
