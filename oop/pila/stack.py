class Stack :
    def __init__ (self):
        self.items = []

    def push(self,elem):
        self.items.append(elem)

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items)==0


p=Stack()
p.push('aa')
p.push('bb')
p.push('cc')
print(p.top())
p.pop()
print(p.top())
p.pop()
print(p.top())
p.pop()

print(p.empty())