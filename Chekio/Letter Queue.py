__author__ = 'Merlo'


def letter_queue(commands):
    newlist = []
    for item in commands:
        if item != "POP":
            newlist.append(item.replace('PUSH ',''))
        else:
            if newlist != []:
                newlist.pop(0)
    return ''.join(newlist)

print letter_queue(["PUSH H", "PUSH I"])