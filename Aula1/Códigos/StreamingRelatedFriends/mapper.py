#!/usr/bin/env python3

import sys

SEP = ':'


class Mapper(object):

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")

    def map(self):
        for person, friends in self:
            friends = friends.rstrip()
            for friend in friends.split(","):
                pair = [person, friend.strip()]
                pair.sort()
                self.emit(pair, friends)

    def __iter__(self):
        for line in self.infile:
            yield line.split(self.sep, 1)


if __name__ == "__main__":
        mapper = Mapper()
        mapper.map()
