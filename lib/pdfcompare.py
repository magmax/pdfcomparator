#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import sys
import poppler


class ComparePDF(object):
    def compare(self):
        return sys.argv[1] == sys.argv[2]


if __name__ == '__main__':
    c = ComparePDF()
    if c.compare():
        exit(0)
    else:
        exit(2)
