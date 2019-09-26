class stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
            return self.items[-1]

    def getstack(self):
        return self.items

s= stack()
s.push("A")
s.push("B")
print(s.getstack())
s.push("C")
print(s.getstack())
s.pop()
print(s.getstack())
print(s.peek())
