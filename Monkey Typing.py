__author__ = 'v_shabalin'


def count_words(text, words):
    count = 0
    text = text.lower()
    for word in words:
        if word in text:
            count += 1
    return count

print count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"})