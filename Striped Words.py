__author__ = 'Merlo'

def checkio(text):
    VOWELS = "AEIOUY"
    CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
    result = ''
    text = text.split(' ')
    for item in text:
        if item.isalpha():
            if (set(item) & set(VOWELS)) != set():
                if (set(item) & set(CONSONANTS)) != set():
                        result = ', '.join(mylist)

    return result

print checkio(u"My name is ...")