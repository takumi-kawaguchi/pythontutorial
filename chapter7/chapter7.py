# formatting
year = 2021
event = 'conference'
print(f'report of the {year} {event}')

s = 'Hello, world.'
print(str(s))
print(repr(s))
print(str(1/7))

hello = 'Hello, world.\n'
print(str(hello))
print(repr(hello))

# optional format operator
import math
print(f'pi is {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
[print(f'{name:10} ==> {phone:10d}') for name, phone in table.items()]

# format()
print('{} says "{}"'.format('he', 'hi'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('this {food} is {adjective}'.format(food='spam', adjective='good'))
[print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3)) for x in range(1, 11)]

# zero fill
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('123456123456'.zfill(7))

# file
f2 = open('test2.txt', 'w')
f2.close()

with open('test.txt') as f:
    read_data = f.read()
    print(read_data)

f.close()

with open('test3.txt') as f3:
    print(f3.read())
    print(f3.read())
f3.close()

with open('test3.txt') as f4:
    print(f4.readline())
    print(f4.readline())
f4.close()

with open('test3.txt') as f5:
    [print(line, end='') for line in f5]
    print()
f5.close()

with open('test4.txt', 'w') as f6:
    print(f6.write('this is test writing'))
f6.close()

# json
import json
x = [1, 'sample', 'list']
print(json.dumps(x))