__author__ = 'v_shabalin'

from math import sqrt
from math import pi
def simple_areas(*args):
    area = 0
    p = 0
    if len(args) == 1:
        area = round((pi*(args[0]**2)/4), 2)
    elif len(args) == 2:
        area = round((args[0] * args[1]), 2)
    else:
        p = (args[0] + args[1] + args[2]) / 2
        area = round((sqrt(p*(p-args[0])*(p-args[1])*(p-args[2]))), 2)
    return area

print simple_areas(1000)