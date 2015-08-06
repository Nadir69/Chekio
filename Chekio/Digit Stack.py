__author__ = 'v_shabalin'

def golf(commands):
    sequence = []
    summ = 0
    for item in commands:
        if item[:3] == 'PUS':
            sequence.append(int(item[5:]))
        elif item[:3] == 'POP':
            if sequence != []:
                summ = summ + int(sequence[-1])
                del sequence[-1]
        else:
            if sequence != []:
                summ += int(sequence[-1])
    return summ

print golf(["PUSH 0","PUSH 1","PUSH 2","PUSH 3","PUSH 4","PUSH 5","PUSH 6","PUSH 7","PUSH 8","PUSH 9"])