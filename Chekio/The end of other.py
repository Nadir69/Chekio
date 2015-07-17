__author__ = 'v_shabalin'


def checkio(words_set):
    for item in words_set:
        for word in (words_set):
            if item != word:
                if item.endswith(word):
                    return True
    return False


print checkio({"hello", "lo", "he"})