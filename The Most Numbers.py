__author__ = 'v_shabalin'


def checkio(*args):
    if args:
        return (max(args) - min(args))
    else:
        return 0

print checkio(10.2, -2.2, 0, 1.1, 0.5)