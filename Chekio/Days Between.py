__author__ = 'v_shabalin'

import string

def check_pangram(text):
    text = text.lower()
    alphabet = string.lowercase
    if (set(alphabet) - set(text)) == set([]):
        return True
    else:
        return False