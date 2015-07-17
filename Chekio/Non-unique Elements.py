__author__ = 'Merlo'


def checkio(data):
    newlist = []
    for item in data:
         if data.count(item) > 1:
             newlist.append(item)
    return newlist

print checkio([1, 2, 3, 1, 3])