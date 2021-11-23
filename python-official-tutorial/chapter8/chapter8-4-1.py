# 例外スロー
raise NameError('HiThere')

# 例外投げ直し
try:
    raise NameError('HiThere')
except NameError:
    print('NameError!')
    raise