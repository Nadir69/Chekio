__author__ = 'v_shabalin'

def checkio(game_result):
    game_result = [str(x) for x in game_result]
    lst = []
    for item in range(len(game_result)):
        game_result[item] = game_result[item].replace('X', '1').replace('O', '0').replace('.', '9')
        game_result[item] = int(game_result[item])

    if sum(game_result[0])
    return game_result


    return game_result

print checkio([
        u"X.O",
        u"XX.",
        u"XOO"])