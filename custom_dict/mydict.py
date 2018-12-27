#!/usr/bin/env python

class MyDict():
    """A custom implementation of the dict object"""

    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def list(self):
        return self.map

    def _get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True

        exists = False
        for kv in self.map[key_hash]:
            if kv[0] == key:
                exists = True

        if exists:
            self.map[key_hash].append(key_value)

        return


    def delete(self, key):
        key_hash = self._get_hash(key)

        for kv in self.map[key_hash]:
            if kv[0]  == key:
                return kv

    def find(self):
        pass


dict1 = MyDict(10)
dict1.add('Beans', 5)
dict1.add('Beans', 10)
dict1.add('Beans', 30)
print(dict1.list())
print(dict1.delete('Beans'))
