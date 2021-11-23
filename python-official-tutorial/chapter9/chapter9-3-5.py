class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

d = Dog('fido')
e = Dog('buddy')

print(d.kind)
print(e.kind)

print(d.name)
print(e.name)