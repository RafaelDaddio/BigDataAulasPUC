#!/usr/bin/env python3

import sys
from itertools import groupby
from operator import itemgetter

SEP = ':'


class Reducer(object):

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")

    def reduce(self):
        mutual_friends = dict()
        for current, group in groupby(self, itemgetter(0)):            
            mutual_friends[current] = list()
            for _, friends in group:
                mutual_friends[current].append(set([friend.strip() for friend in friends.split(",")]))
            self.emit(current, mutual_friends[current][0].intersection(mutual_friends[current][1]))

    def __iter__(self):
        for line in self.infile:
            #print(line)
            yield line.split(self.sep, 1)


if __name__ == "__main__":
    reducer = Reducer()
    reducer.reduce()
