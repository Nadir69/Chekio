def checkio(numbers_array):
    return sorted(numbers_array, key=abs)

print checkio((-1, -2, -3, 0))