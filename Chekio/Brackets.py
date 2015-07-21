__author__ = 'v_shabalin'

import string

def checkio(expression):
    chars = string.digits + '+-*/'
    a = ['(', ')']
    b = ['{', '}']
    c = ['[', ']']
    for item in chars:
        expression = expression.replace(item, '')
    count = 0
    while count < len(expression):
        if expression[count] == a[1] and expression[count-1] == a[0]:
            expression = expression[:count-1] + expression[count+1:]
            count = 0
        elif expression[count] == b[1] and expression[count-1] == b[0]:
            expression = expression[:count-1] + expression[count+1:]
            count = 0
        elif expression[count] == c[1] and expression[count-1] == c[0]:
            expression = expression[:count-1] + expression[count+1:]
            count = 0
        else:
            count += 1
    if len(expression) == 0:
        return True
    else:
        return False

print checkio("[{(((((({[[{{(({()}))}}]]}))))))}]")