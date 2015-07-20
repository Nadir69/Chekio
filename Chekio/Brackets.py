__author__ = 'v_shabalin'

import string

def checkio(expression):
    chars = string.digits + '+-*/'
#    expression = list(expression)
    for item in range(len(expression)):
        expression = expression.replace(chars[item], '')
    return expression


print checkio("((5+3)*2+1)")