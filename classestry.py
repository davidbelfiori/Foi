'''create classes in python '''
class geometira:
    def rectangle(self, length, width):
        self.length = length
        self.width = width
        return self.length * self.width
    
    def square(self, side):
        self.side = side
        return self.side * self.side
    
    def triangle(self, base, height):
        self.base = base
        self.height = height
        return 0.5 * self.base * self.height