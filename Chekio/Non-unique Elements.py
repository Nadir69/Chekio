__author__ = 'Merlo'

import string

def checkio(data):
    newlist = []
    for item in data:
         if data.count(item) > 1 or ((str(item).upper() in data) and (str(item).lower() in data)):
             newlist.append(item)
    return newlist

print checkio(['X', 'H', 'e', 'V', 'm', 'l', 's', 1, 0, 'y', 'j', 'b', 'g', 'o', 'R', 'U', 'O', 'p', 'p', 8, 'Y', 'B', 'Y', 'O', 'r', 'E', 't', 'I', 'w', 'i', 'v', 'o', 2, 'd', 'Z', 'b', 'S', 'T', 'n', 0])