__author__ = 'Merlo'

import re

def checkio(text):
    VOWELS = "AEIOUY".lower()
    CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ".lower()
    result = 0
    text = re.findall(r"[\w']+", text.lower()) #splitting string by punctuation and spaces
    for item in text:
        if item.isalpha() and len(item) > 1:
            if item[0] in VOWELS:
                if (set(item[::2]) < set(VOWELS)) == True and (set(item[1::2]) < set(CONSONANTS)) == True:
                    result += 1
            else:
                if (set(item[::2]) < set(CONSONANTS)) == True and (set(item[1::2]) < set(VOWELS)) == True:
                    result += 1

    return result

print checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?")