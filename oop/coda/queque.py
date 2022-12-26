class queque:
    def __init__(self):
        self.item=[]
    def inn(self, elem):
        self.item.append(elem)

    def out(self):
        self.item.pop(0)
    def frist(self):
        return self.item[0]

    def last(self):
        return self.item[-1]

    def empty(self):
        return len(self.item)==0

p= queque()

p.inn('aa')
p.inn('bb')
p.inn('cc')
print(p.item)
print(p.frist())
print(p.last())
p.out()
print(p.frist())
print(p.last())
