class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w1.purpose, w1.region)
print(w2.purpose, w2.region)

def f1(self, x, y):
    return min(x, x + y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

c = C()
print(c.f(2, 3))
print(c.g())
print(c.h())
