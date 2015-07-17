__author__ = 'v_shabalin'

def checkio(opacity):
    array = [0,1,1]
    age = 0
    transparency = 10000
    while transparency != opacity:
        if age in array:
            transparency -= age
        else:
            transparency += 1
        age += 1
        array.append(array[-2]+array[-1])
    return age - 1


print checkio(9999)