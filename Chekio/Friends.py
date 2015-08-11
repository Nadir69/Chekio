__author__ = 'v_shabalin'

class Friends:
    def __init__(self, connections):
        self.connections = connections
        pass

    def add(self, connection):
        self.connections = list(self.connections)
        if connection not in self.connections:
            self.connections.append(connection)
            return True
        return False

    def remove(self, connection):
        self.connections = list(self.connections)
        for item in self.connections:
            if item == connection:
                del self.connections[self.connections.index(item)]
                return True
        return False

    def names(self):
        result = set()
        for item_group in self.connections:
            for item in item_group:
                result.add(item)
        return result

    def connected(self, name):
        result = set()
        self.connections = list(self.connections)
        for item_group in self.connections:
            item_group = list(item_group)
            if name in item_group:
                if item_group[0] == name:
                    result.add(item_group[1])
                else:
                    result.add(item_group[0])
        return result

    def __repr__(self):
        return str(self.connections)



f = Friends([{"1", "2"}, {"3", "1"}])
print f.add({"4", "5"})
print f
#
# f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
# print f.add({"sophia", "stephen"})
# print f.remove({"sophia", "nikola"})
# f.connected("sophia")