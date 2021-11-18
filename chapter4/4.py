# if文
# x = int(input("please enter an integer: "))
# if x < 0:
#     x = 0
#     print("negative changed to zero")
# elif x == 0:
#     print("zero")
# else:
#     print("natural num")
# print("x =", x)

# for文
# words = ["penguine", "window", "apple"]
# for w in words:
#     print(w, len(w))

# for i in range(5):
#     print(i)

# range(開始位置, 最大値, 増加量)
# for j in range(5, 10):
#     print(j)

# for k in range(0, 10, 3):
#     print(k)

# a = ["alice", "bob", "charlie"]
# for i in range(len(a)):
#     print(i, a[i])

# forのelse
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         print(n, 'is a prime number')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print('even num:', num)
#         continue
#     print('odd num:', num)

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
fib(2000)