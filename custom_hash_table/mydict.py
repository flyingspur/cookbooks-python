#!/usr/bin/env python

class MyDict():
    """A custom implementation of the dict object
    """
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def list(self):
        return self.map

    def add(self, key, value):
        kv = [key, value]

        for l in range(0, len(self.map)):
            if self.map[l] is not None:
                k = self.map[l][0][0]
                if k == key:
                    self.map[l].append(kv)
                    return True
            if self.map[l] is None:
                self.map[l] = list([kv])
                return True
        else:
            return False

    def delete(self, key):
        for l in range(0, len(self.map)):
            if self.map[l] is not None:
                k = self.map[l][0][0]
                if k == key:
                    self.map[l] = None
                    return True
        else:
            return False

    def find(self, key):
        for l in range(0, len(self.map)):
            if self.map[l] is not None:
                k = self.map[l][0][0]
                if k == key:
                    return self.map[l]
        else:
            return False

