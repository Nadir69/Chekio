__author__ = 'v_shabalin'

def verify_anagrams(first_word, second_word):
    first_word = first_word.replace(' ','').lower()
    second_word = second_word.replace(' ','').lower()
    if ''.join(sorted(first_word)) == ''.join(sorted(second_word)):
        return True
    else:
        return False

print verify_anagrams(u"Hello", u"Ole Oh")