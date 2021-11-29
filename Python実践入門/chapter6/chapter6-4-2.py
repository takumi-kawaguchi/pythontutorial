class A:
    def hello(self):
        print('hello')

class B(A):
    def hello(self):
        print('hola')
        super().hello()

class C(A):
    def hello(self):
        print('ニーハオ')
        super().hello()

class D(B, C):
    def hello(self):
        print('こんにちは')
        super().hello()

d = D()
d.hello()
print(D.__mro__)