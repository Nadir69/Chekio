__author__ = 'v_shabalin'


def left_join(phrases):
    string = ",".join(phrases)
    string = string.replace("right","left")
    return string

print left_join(("left", "right", "left", "stop"))