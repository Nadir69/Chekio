__author__ = 'v_shabalin'
import string

def checkio(text):
    punct = string.punctuation + string.digits + " "
    text = text.lower()
    for char in text:
        if char in punct:
            text = text.replace(char, '')

    return text


print checkio(u"Hello World!")


>>> s = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'q', 'a', 'z', 'x', 'd', 'e', 'r', 'f', 'x', 's', 'a', 'w', 'e', 'd', 's']
>>> from collections import Counter
>>> c=Counter(s)
>>> c = Counter(s)