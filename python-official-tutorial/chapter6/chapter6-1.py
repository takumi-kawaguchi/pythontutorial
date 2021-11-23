# fiboはシンボルテーブルに定義しない、そのまま関数を取り込む
# from fibo import * のような記述もできるが、無暗にすべて取り込むと名前がバッティングする可能性あるので非推奨

# from fibo import fib, fib2
# print(fib(1000))

# asで別名を付与できる
import fibo as fib
print(fib.fib(10000))

from fibo import fib as fibonacci
print(fibonacci(20000))