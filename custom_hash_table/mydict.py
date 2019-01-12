#!/usr/bin/env python

class MyDict():
"""A custom implementation of the dict object
"""
    def __init__(self, size):
        self.size = size
        self.map = [None] * size

    def list(self):
        return self.map

    def add(self, key, value):
        key_value = [key, value]

        for i in range(0, self.size):
            if self.map[i] is None:
                self.map[i] = list([key_value])
                return True
            else:
                k = self.map[i][0][0]
                if k == key:
                    self.map[i].append(key_value)
                    return True
                else:
                    continue
        return False

    def delete(self, key):
        for i in range(0, self.size):
            k = self.map[i][0][0]
            if k == key:
                self.map.pop(i)
                return True
        return False
