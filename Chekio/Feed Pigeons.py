__author__ = 'v_shabalin'

def checkio(food):
    pigeons = 1
    count = 1
    while food > pigeons:
        food -= pigeons
        count += 1
        pigeons += count
    else:
        if food > (pigeons - count):
            return food
        else:
            return pigeons - count


print checkio(10)
