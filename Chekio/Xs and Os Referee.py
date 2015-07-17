__author__ = 'v_shabalin'

def checkio(game_result):
    newlist = ''.join(game_result)
    combos = ['012', '345', '678', '036', '147', '258', '480', '246']
    for item in combos:
        if newlist[int(item[0])] == newlist[int(item[1])] == newlist[int(item[2])] and newlist[int(item[0])] != '.':
            return newlist[int(item[0])]
    return 'D'


print checkio([
        u"X.O",
        u"XX.",
        u"XOO"])