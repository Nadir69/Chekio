__author__ = 'v_shabalin'

def count_inversion(sequence):
    total = 0
    for item in sequence:
        for itm in sequence[sequence.index(item):]:
            if item > itm:
                total += 1
    return total

print count_inversion((5, 3, 2, 1, 0))
