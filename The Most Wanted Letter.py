__author__ = 'Merlo'

import string

def checkio(text):
    text = text.lower()
    remove = string.digits + string.punctuation + ' '
    for char in text:
        if char in remove:
            text = text.replace(char, '')
    text = sorted(text)
    result = ""
    count = 0
    for item in text:
        if text.count(item) > count:
            count = text.count(item)
            result = item

    return result