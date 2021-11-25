class Klass:
    def __new__(cls, *args):
        print(f'cls={cls}')
        print('new', args)
        return super().__new__(cls)
    def __init__(self, *args):
        print('init', args)

kls = Klass(1, 2, 3)

# インスタンスの作成自体は__new__で行って返却するので、__new__の返り値を操作すればインスタンス化されない
class Evil:
    def __new__(cls, *args):
        return 1

evil = Evil()
print(isinstance(evil, Evil))
print(type(evil))
print(evil)