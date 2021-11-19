# リスト
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('ramen'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)

from collections import deque
queue = deque(['alice', 'bob', 'charlie'])
queue.append('daisy')
print(queue)
queue.popleft()
print(queue)

# リスト内包表記
squares = list(map(lambda x: x**2, range(10)))
print(squares)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([x.strip() for x in freshfruit])

print([(x, x**2) for x in range(6)])

tdlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(num for elem in tdlist for num in elem)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print([[row[i] for row in matrix] for i in range(4)])

# タプル
t = 12345, 67890, 'hello'
print(t[0])
print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(singleton)

x, y, z = t
print(x)
print(y)
print(z)

# 辞書型
tel = { "jack": 4098, "sape": 4139 }
tel["guido"] = 4127
print(tel)
del tel["sape"]
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('guido' not in tel)

knights = { "gallahad": "the pure", "robin": "the brave" }
for k, v in knights.items():
    print(k, v)

[print(k2, v2) for k2, v2 in knights.items()]

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
[print('what is your {0}? - it is {1}.'.format(q, a)) for q, a in zip(questions, answers)]

[print(i) for i in reversed(range(1, 10, 2))]

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
[print(fruit) for fruit in sorted(set(basket))]

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
[filtered_data.append(value) for value in raw_data if not math.isnan(value)]
print(filtered_data)

