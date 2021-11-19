# if文
x = int(input("please enter an integer: "))
if x < 0:
    x = 0
    print("negative changed to zero")
elif x == 0:
    print("zero")
else:
    print("natural num")
print("x =", x)

# for文
words = ["penguine", "window", "apple"]
for w in words:
    print(w, len(w))

for i in range(5):
    print(i)

range(開始位置, 最大値, 増加量)
for j in range(5, 10):
    print(j)

for k in range(0, 10, 3):
    print(k)

a = ["alice", "bob", "charlie"]
for i in range(len(a)):
    print(i, a[i])

# forのelse
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print('even num:', num)
        continue
    print('odd num:', num)

# 関数定義
def fib(n):
    """print fib"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
fib(2000)
print(fib(0))

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = fib2(100)
print(f100)

def ask_ok(prompt, retries = 4, reminder = 'please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user repsonse')
        print(reminder)

ask_ok("test")

def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def concat(*args ,sep="/"):
    return sep.join(args)
print(concat("earth", "mars", "venus"))

# ラムダ
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(1))
print(f(84))

pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# docstring
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


def test(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


test('spam')
