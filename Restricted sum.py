__author__ = 'v_shabalin'

def checkio(data):
    if len(data) != 1:
        data[0] = data[0] + data[-1]
        del data[-1]
        checkio(data)
    return data[0]


print checkio([2, 2, 2, 2, 2, 2])