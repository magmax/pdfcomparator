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

from __future__ import print_function
import os
import sys
import argparse
import poppler
import cairo


class PDFCompareError(Exception):
    pass


class DifferentNumberOfPages(PDFCompareError):
    def __init__(self, pages_a, pages_b, *args, **kwargs):
        super(DifferentNumberOfPages, self).__init__(*args, **kwargs)
        self.pages_a = pages_a
        self.pages_b = pages_b

    def __str__(self):
        return 'Different number of pages ({0} vs {1})'.format(self.pages_a, self.pages_b)


class DifferentPage(PDFCompareError):
    def __init__(self, page, *args, **kwargs):
        super(DifferentPage, self).__init__(*args, **kwargs)
        self.page = page

    def __str__(self):
        return 'Page {0} is different.'.format(self.page)


class ComparePDF(object):
    def __init__(self, file_a, file_b):
        self.file_a = file_a
        self.file_b = file_b

    def compare(self):
        try:
            self._try_compare()
            return True
        except PDFCompareError as e:
            print(e)
            return False
        except:
            return False

    def _try_compare(self):
        doc_a = self._load_file(self.file_a)
        doc_b = self._load_file(self.file_b)

        self._assert_same_page_number(doc_a, doc_b)
        self._assert_all_pages_are_equal(doc_a, doc_b)

    def _assert_same_page_number(self, doc_a, doc_b):
        pages_a = doc_a.get_n_pages()
        pages_b = doc_b.get_n_pages()

        if pages_a is not pages_b:
            raise DifferentNumberOfPages(pages_a, pages_b)

    def _assert_all_pages_are_equal(self, doc_a, doc_b):
        for i in xrange(doc_a.get_n_pages()):
            pagea0 = doc_a.get_page(i)
            pageb0 = doc_b.get_page(i)

            if self._render(pagea0) != self._render(pageb0):
                raise DifferentPage(i+1)

    def _load_file(self, filename):
        path = os.path.realpath(filename)
        uri = "file://{0}".format(path)
        return poppler.document_new_from_file(uri, None)

    def _render(self, page):
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
