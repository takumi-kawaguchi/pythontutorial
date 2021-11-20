def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# モジュールとして取り込まれるのではなく、
# このファイルがスクリプトとして実行された際に呼び出される処理
if __name__ == "__main__":
    import sys
    print(__name__)
    print(sys.argv[0])
    print(fib(int(sys.argv[1])))
    print(sys.path)