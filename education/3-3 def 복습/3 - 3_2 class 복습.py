class Clac:
    def __init__(self, a_class, b):
        self.a = a_class
        self.b = b

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a + self.b

    def multriple(self):
        return self.a + self.b

    def divaid(self):
        return self.a + self.b


a = Clac(3, 5)

print(a.a, a.b, a.multriple(), a.plus(), a.minus(), a.divaid())