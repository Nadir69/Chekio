__author__ = 'v_shabalin'


def check_grid(grid):
    result = 0
    for line in grid:
        result += check_line(line)
    for line in zip(*grid):
        result += check_line(line)
    if result < 1:
        return True
    else:
        return False
def check_line(line):
    result = 0
    for item in line[0::2]:
        if item != line[0]:
            result += 1
    for item in line[1::2]:
        if item != line[1] or item == line[0]:
            result += 1
    return result

print check_grid([["X", "Z", "X", "Z"],
                       ["Z", "X", "Z", "X"]])