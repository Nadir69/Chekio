__author__ = 'v_shabalin'

def swap_sort(array):
    array = list(array)
    a = len(array)
    result = ''
    while array != sorted(array):
        for item in range(len(array)-1):
            if array[item] > array[item+1]:
                array[item], array[item+1] = array[item+1], array[item]
                result +=  ',' + str(item) + str(item+1)
    result = result.replace(',', '', 1)
    return result


print swap_sort((6, 4, 2))