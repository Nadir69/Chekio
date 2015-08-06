__author__ = 'v_shabalin'

def count_ingots(report):
    digits = range(1,10)
    alphabet = map(chr, range(65, 91))
    array = []
    result = 0
    for character in alphabet:
        for digit in digits:
            array.append(character + str(digit))
    report = report.split(',')
    for item in report:
        result += len(array[:(array.index(item))+1])
    return result

print count_ingots("C1,D1,B1,E1,F1")