#!/usr/bin/env python3

import sys
import os
import re

SEP = '\t'


class Mapper(object):

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

        self.stopwords = set()
        self.tokenizer = re.compile(r'\W+')

        with open('/home/bigdata-vm/Desktop/BigDataAulasPUC/Aula2/Códigos/TF-IDF/stopwords') as stop:
            for line in stop:
                self.stopwords.add(line.rstrip())


    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")

    def tokenize(self, line):
        for word in re.split(self.tokenizer, line):
            if word and word.lower() not in self.stopwords and word.isalpha():
                yield word.lower()


    def map(self):
        for line in self:

            file_name = os.getenv('map_input_file')
            for word in self.tokenize(line):
                self.emit((word, file_name), 1)


    def __iter__(self):
        for line in self.infile:
            yield line.rstrip()


if __name__ == "__main__":
    mapper = Mapper()
    mapper.map()
