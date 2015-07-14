__author__ = 'v_shabalin'

def checkio(game_result):
    result = []
    for row in range(len(game_result)):
        for column in range(len(game_result[0])):
            if game_result[row][column] == "X":
                result[row][column] = 1
            elif game_result[row][column] == "O":
                result[row][column] = 0
            else:
                result[row][column] = 9
    return result

print checkio([
        u"X.O",
        u"XX.",
        u"XOO"])