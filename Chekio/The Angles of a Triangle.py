__author__ = 'v_shabalin'

from math import acos, degrees

def checkio(a, b, c):
    result = []
    pairs = [[a,b,c], [a,c,b], [b,c,a]]
    for item in pairs:
        if (item[0] + item[1]) > item[2]:
            angle_acos = float(item[0]**2 + item[1]**2 - item[2]**2) / float(2 * item[0] * item[1])
            angle_acos = int(round(degrees(acos(angle_acos))))
            result.append(angle_acos)
        else:
            return [0, 0, 0]
    return sorted(result)

print checkio(2, 2, 5)