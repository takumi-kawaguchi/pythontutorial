import base64

def str_to_base64(x):
    '''convert string to base64 expression'''
    return base64.b64encode(x.encode('utf-8'))