__author__ = 'v_shabalin'


def checkio(number):
    number = str(number)
    number = number.replace("0","")
    total = 1
    for item in number:
        total = total * int(item)
    return total

print checkio(1111)