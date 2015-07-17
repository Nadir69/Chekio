__author__ = 'v_shabalin'


def boolean(x, y, operation):
    if operation == "conjunction":
        return (x and y)
    elif operation == "disjunction":
        return (x or y)
    elif operation == "implication":
        return int(not (x >> y))
    elif operation == "exclusive":
        return (x ^ y)
    else:
        return int(not (x ^ y))

print boolean(1, 0, u"conjunction")
print boolean(1, 0, u"disjunction")
print boolean(1, 1, u"implication")
print boolean(0, 1, u"exclusive")
print boolean(0, 1, u"equivalence")