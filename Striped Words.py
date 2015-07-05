__author__ = 'Merlo'

def checkio(text):
    VOWELS = "AEIOUY".lower()
    CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ".lower()
    result = 0
    text = (text.lower()).split(' ')
    for item in text:
        if item.isalpha():
            if (set(item) & set(VOWELS)) != set():
                if (set(item) & set(CONSONANTS)) != set():
                    result += 1

    return result

print checkio(u"Hello world")