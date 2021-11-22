# 例外の連鎖
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('failed to open database') from exc