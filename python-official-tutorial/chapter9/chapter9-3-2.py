class MyClass:
    i = 12345

    def __init__(self):
        self.data = [1, 2, 3]

    def f(self):
        return 'hello, world'

x = MyClass()
print(x.i)
print(x.f())
print(x.data)

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

y = Complex(3.0, -4.5)
print(y.r, y.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

xf = x.f
print(xf())