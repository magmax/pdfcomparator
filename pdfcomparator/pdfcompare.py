#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

# Copyright Miguel Angel Garcia <miguelangel.garcia@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import argparse
import poppler
import cairo



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


def main():
    parser = argparse.ArgumentParser(description='Compares two PDF files.')
    parser.add_argument('file', nargs=2,
                        help='PDF files to be compared')

    args = parser.parse_args()

    for f in args.file:
        if not os.path.exists(f):
            parser.error('File %s does not exist' % f)

    c = ComparePDF(*args.file)
    if c.compare():
        exit(0)
    else:
        exit(2)

if __name__ == '__main__':
        main()
