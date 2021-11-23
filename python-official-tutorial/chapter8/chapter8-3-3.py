import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('OSError: {0}'.format(err))
except ValueError:
    print('ValueError: invalid value')
except:
    print('UnexpectedError')
    raise