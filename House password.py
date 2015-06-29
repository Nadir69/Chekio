__author__ = 'v_shabalin'
import string

def checkio(data):
    integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    upperceases = list(string.ascii_uppercase)
    lowerceases = list(string.ascii_lowercase)
    data = list(data)
    if len(data) < 10:
        return False
    newuppercases = []
    newlowerceases = []
    newintegers = []
    for letter in data:
        if letter in upperceases:
            newuppercases.append(letter)
        elif letter in lowerceases:
            newlowerceases.append(letter)
        elif letter in integers:
            newintegers.append(letter)
        else:
            return "Wrong symbol"
    if newuppercases == [] or newlowerceases == [] or newintegers == []:
        return False
    else:
        return True

print checkio('ULFFunH8ni')