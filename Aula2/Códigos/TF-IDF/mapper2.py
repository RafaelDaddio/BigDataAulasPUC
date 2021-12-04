#!/usr/bin/env python3

import sys
import ast

SEP = '\t'


class Mapper(object):

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")

    def map(self):
        for line in self:
            key, tf = line.split(self.sep)
            tf = int(tf)
            word, doc = ast.literal_eval(key)
            self.emit(word, (doc, tf, 1))

    def __iter__(self):
        for line in self.infile:
            yield line.rstrip()


if __name__ == "__main__":
    mapper = Mapper()
    mapper.map()
