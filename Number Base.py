__author__ = 'Merlo'

def checkio(str_number, radix):
    try:
        return int(str_number, base=radix)
    except ValueError:
        return "Oops!  That was no valid number.  Try again..."

print checkio("101", 2)