__author__ = 'v_shabalin'

def count_neighbours(grid, row, col):
    total = 0
    neighbours = ((row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1))
    for neighbour in neighbours:
        if (neighbour[0] < len(grid) and neighbour[1] < len(grid[0])) and neighbour[0] >= 0 and neighbour[1] >= 0:
            if grid[neighbour[0]][neighbour[1]] == 1:
                total += 1
    return total

print count_neighbours(
    ((1,0,1,0,1),
     (0,1,0,1,0),
     (1,0,1,0,1),
     (0,1,0,1,0),
     (1,0,1,0,1),
     (0,1,0,1,0),), 5, 4)