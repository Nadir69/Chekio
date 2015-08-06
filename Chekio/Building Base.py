__author__ = 'v_shabalin'

class Building:

def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        d = {}
        d['north-west'] = [self.south+self.width_NS, self.west]
        d['north-east'] = [self.south+self.width_NS, self.west+self.width_WE]
        d['south-west'] = [self.south, self.west]
        d['south-east'] = [self.south, self.west+self.width_WE]
        return d

    def area(self):
        return self.width_NS * self.width_WE

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return "Building({}, {}, {}, {}, {})".format(self.south, self.west, self.width_WE, self.width_NS, self.height)



print Building(1, 2, 2, 2).corners()
print Building(1, 2.5, 4.2, 1.25).area()
#print Building(10, 10, 1, 2, 2).Building
print Building(1, 2.5, 4.2, 1.25, 101).volume()
print str(Building(0.2, 1, 2, 2.2, 3.5))