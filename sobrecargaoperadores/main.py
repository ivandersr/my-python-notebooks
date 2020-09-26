class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<class Retangulo({self.x}, {self.y})>"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Retangulo(x, y)

    def __gt__(self, other):
        return self.x * self.y > other.x * other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


r1 = Retangulo(10, 20)
r2 = Retangulo(20, 10)
r3 = Retangulo(20, 10)
print(r1 == r2)
print(r2 == r3)
