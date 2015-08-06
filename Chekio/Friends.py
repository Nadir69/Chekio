__author__ = 'v_shabalin'

class Friends:
    def __init__(self, connections):
        self.connections = connections
        pass

    def add(self, connection):
        if connection not in self.connections:
            self.connections = list(self.connections).append(connection)
            return True
        return False

    def remove(self, connection):
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
        for item_group in self.connections:
            if name in item_group:
                if item_group[0] == name:
                    result.add(item_group[1])
                else:
                    result.add(item_group[0])
        return result


letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})).add({"c", "d"})
digit_friends = Friends([{"1", "2"}, {"3", "1"}])
print letter_friends
assert letter_friends.add({"c", "d"}) is True, "Add"
assert letter_friends.add({"c", "d"}) is False, "Add again"
assert letter_friends.remove({"c", "d"}) is True, "Remove"
assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
assert letter_friends.names() == {"a", "b", "c"}, "Names"
assert letter_friends.connected("d") == set(), "Non connected name"
assert letter_friends.connected("a") == {"b", "c"}, "Connected name"