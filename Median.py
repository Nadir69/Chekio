__author__ = 'Merlo'


def checkio(data):
    data.sort()
    if len(data) % 2 == 0:
         return (data[len(data)/2] + data[len(data)/2 - 1]) / 2.0
    else:
        return data[len(data)/2]

print checkio([3, 6, 20, 99, 10, 15])