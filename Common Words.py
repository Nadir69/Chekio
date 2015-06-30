__author__ = 'v_shabalin'

def checkio(first, second):
    first = set(first.split(","))
    second = set(second.split(","))
    result = sorted(list(first & second))
    return ','.join(result)

print checkio(u"one,two,three", u"four,five,one,two,six,three")