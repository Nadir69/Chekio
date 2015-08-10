__author__ = 'v_shabalin'

def checkio(number):
    pigeons = 1 #how much pigeons eat per minute
    count = 1
    while number >= pigeons:
        number -= pigeons
        count += 1
        pigeons += count
    return pigeons - count

print checkio(20)
