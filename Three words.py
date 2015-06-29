__author__ = 'v_shabalin'


def checkio(words):
    words = words.split()
    count = 0
    for item in words:
        if item.isalpha():
            count += 1
            if count > 2:
                return True
        else:
            count = 0
    return False

print checkio("one two 3 four five six 7 eight 9 ten eleven 12")