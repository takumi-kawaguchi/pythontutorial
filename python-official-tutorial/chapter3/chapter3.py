# ヒアドキュメント
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 文字列リテラルの自動連結
print('Put several strings within parentheses '
      'to have them joined together.')

# スライス
lang = "Python"
print(lang[0:2])
print(lang[2:5])
print(lang[:2] + lang[2:])

# リスト
squares = [1, 4, 9, 16, 25]
copiedSquares = squares[:]
print(squares)
print(copiedSquares)

squares[1] = 36
print(squares)
print(copiedSquares)

squares.append(6**2)
print(squares)
print(len(squares))

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b