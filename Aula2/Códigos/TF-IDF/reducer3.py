#!/usr/bin/env python3

import sys
from itertools import groupby
from operator import itemgetter

SEP = '\t'


class Reducer(object):

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")

    def reduce(self):
        for key, values in self:
            for value in values:
                self.emit(key, value)

    def read(self):
        for line in self.infile:
            yield line.rstrip()

    def __iter__(self):
        generator = (line.split(self.sep, 1) for line in self.read())
        for key, values in groupby(generator, itemgetter(0)):
            yield key, [value[1] for value in values]

if __name__ == "__main__":
    reducer = Reducer()
    reducer.reduce()
