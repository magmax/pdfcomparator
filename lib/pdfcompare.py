#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import os
import sys
import poppler
import cairo
import io

class ComparePDF(object):
    def __init__(self, file_a, file_b):
        self.file_a = file_a
        self.file_b = file_b

    def compare(self):
        try:
            return self.__try_compare()
        except:
            return False

    def __try_compare(self):
        doc_a = self.__load_file(self.file_a)
        doc_b = self.__load_file(self.file_b)

        if not self.__have_same_page_number(doc_a, doc_b):
            return False

        if not self.__all_pages_are_equal(doc_a, doc_b):
            return False

        return True

    def __have_same_page_number(self, doc_a, doc_b):
        pages_a = doc_a.get_n_pages()
        pages_b = doc_b.get_n_pages()

        if pages_a is pages_b:
            return True

        print 'Different number of pages ({0} vs {1})'.format(pages_a, pages_b)

        return False

    def __all_pages_are_equal(self, doc_a, doc_b):
        for i in xrange(doc_a.get_n_pages()):
            pagea0 = doc_a.get_page(i)
            pageb0 = doc_b.get_page(i)

            if self.__render(pagea0) != self.__render(pageb0):
                print 'Page {0} is different.'.format(i+1)
                return False
        return True

    def __load_file(self, filename):
        path = os.path.realpath(filename)
        uri = "file://{0}".format(path)
        return poppler.document_new_from_file(uri, None)

    def __render(self, page):
        size = page.get_size()
        surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, int(size[0]), int(size[1]))
        context = cairo.Context(surface)
        page.render(context)
        return surface.get_data()


def print_help():
    print "Format: pdfcompare.py file1 file2"
    exit(1)

def main():
    if len (sys.argv) < 3:
        print_help()

    c = ComparePDF(sys.argv[1], sys.argv[2])
    if c.compare():
        exit(0)
    else:
        exit(2)

if __name__ == '__main__':
        main()
