#!/usr/bin/env python3

import sys
import ast
import math

SEP = '\t'

class Mapper(object):

    def __init__(self, infile=sys.stdin, separator=SEP, N=41):
        self.infile = infile
        self.sep = separator
        self.n = N

    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")

    def map(self):
        for line in self:
            key, value = map(ast.literal_eval, line.split(self.sep))
            tf, df = (int(x) for x in value)
            if df > 0:
                idf = math.log(self.n/df)
                self.emit(key, tf*idf)


    def __iter__(self):
        for line in self.infile:
            yield line.rstrip()


if __name__ == "__main__":
    mapper = Mapper()
    mapper.map()
