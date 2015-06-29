__author__ = 'Merlo'


def weak_point(matrix):
    x = 0
    y = 0
    sumx = 0
    sumy = 0
    for x in range(len(matrix)):
        sumx += sum(matrix[x])