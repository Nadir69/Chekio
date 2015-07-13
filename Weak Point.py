__author__ = 'Merlo'


def weak_point(matrix):
    sumx = [sum(row) for row in matrix]
    sumy = [sum(column) for column in zip(*matrix)]
    return sumx.index(min(sumx)), sumy.index(min(sumy))

def weak_point(matrix):
    sumx = map(sum, matrix)
    sumy = map(sum, zip(*matrix))
    return sumx.index(min(sumx)), sumy.index(min(sumy))


print weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])