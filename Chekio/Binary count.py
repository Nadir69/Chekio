__author__ = 'Merlo'

def checkio(number):
    return bin(number).count("1")

print checkio(1022)