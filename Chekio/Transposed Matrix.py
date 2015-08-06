__author__ = 'v_shabalin'

def checkio(data):
    result = []
    for item in zip(*data):
        result.append(list(item))
    return result

print checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]])