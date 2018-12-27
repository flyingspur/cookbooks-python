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

        temp_map = self.map[key_hash].copy()

        for i,v in enumerate(temp_map):
            if key == v[0]:
                self.map[key_hash].pop(0)

        if len(self.map[key_hash]) == 0:
            self.map[key_hash] = None

        return

    def find(self, key):
        key_hash = self._get_hash(key)

        try:
            for i,v in enumerate(self.map[key_hash]):
                if key == v[0]:
                    return self.map[key_hash]
        except:
            print('Key ' + key + ' does not exist.')
            return False

        return False


dict1 = MyDict(10)
dict1.add('Pencils', 5)
dict1.add('Pens', 10)
dict1.add('Pens', 20)
dict1.add('Erasers', 30)
print("ADD: List of items: ", dict1.list())
dict1.delete('Pencils')
print("DELETE: List of items: ", dict1.list())
print("FIND: Item: ", dict1.find('Pens'))
