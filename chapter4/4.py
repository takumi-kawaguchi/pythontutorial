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
for j in range(5, 10):
    print(j)

for k in range(0, 10, 3):
    print(k)

a = ["alice", "bob", "charlie"]
for i in range(len(a)):
    print(i, a[i])