class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    def isEmpty(self):
        return len(self.items) ==0


stack = Stack()
stack.push("First item")
stack.push("Second item")
print(stack.peek())
stack.pop()
print(stack.peek(), "2nd print")