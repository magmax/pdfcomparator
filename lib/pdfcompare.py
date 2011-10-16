#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import os
import sys
import poppler


class ComparePDF(object):
    def compare(self, a, b):
        if a == b:
            return True

        doc_a = self.__load_file(a)
        doc_b = self.__load_file(b)

        return doc_a.get_n_pages() == doc_b.get_n_pages()

    def __load_file(self, filename):
        uri = "file://{0}".format(os.path.realpath(filename))
        return poppler.document_new_from_file(uri, None)



def print_help():
    print "Format: "
    exit(1)

def main():
    c = ComparePDF()
    if len (sys.argv) < 3:
        print_help()

    if c.compare(sys.argv[1], sys.argv[2]):
        exit(0)
    else:
        exit(2)

if __name__ == '__main__':
        main()
