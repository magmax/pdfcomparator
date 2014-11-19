import unittest
import pexpect

COMMAND = 'python pdfcomparator/pdfcompare.py %s %s'

EXAMPLE1a = 'tests/patterns/example1a.pdf'
EXAMPLE1b = 'tests/patterns/example1b.pdf'
EXAMPLE2a = 'tests/patterns/example2a.pdf'
EXAMPLE2b = 'tests/patterns/example2b.pdf'
EXAMPLE3a = 'tests/patterns/example3a.pdf'
EXAMPLE3b = 'tests/patterns/example3b.pdf'
EXAMPLE4a = 'tests/patterns/example4a.pdf'
EXAMPLE4b = 'tests/patterns/example4b.pdf'


class UsageTest(unittest.TestCase):
    def test_no_parameters(self):
        self.sut = pexpect.spawn(COMMAND % ('', ''))
        self.sut.expect("error: too few arguments", timeout=1)

    def test_just_one_parameter(self):
        self.sut = pexpect.spawn(COMMAND % ('foo', ''))
        self.sut.expect("error: too few arguments", timeout=1)

    def test_two_invalid_parameters(self):
        self.sut = pexpect.spawn(COMMAND % ('foo1', 'foo2'))
        self.sut.expect("error: File foo1 does not exist", timeout=1)


class ComparitionTest(unittest.TestCase):
    def test_compared_to_itself(self):
        self.sut = pexpect.spawn(COMMAND % (EXAMPLE1a, EXAMPLE1a))
        assert self.sut.wait() == 0

    def test_compared_to_different(self):
        self.sut = pexpect.spawn(COMMAND % (EXAMPLE1a, EXAMPLE2a))
        self.sut.expect("Different number of pages", timeout=2)
        assert self.sut.wait() == 2

    def test_compared_to_similar(self):
        self.sut = pexpect.spawn(COMMAND % (EXAMPLE1a, EXAMPLE1b))
        assert self.sut.wait() == 0

    def test_compared_to_similar_with_several_pages(self):
        self.sut = pexpect.spawn(COMMAND % (EXAMPLE2a, EXAMPLE2b))
        assert self.sut.wait() == 0

    def test_different_1_page_docs(self):
        self.sut = pexpect.spawn(COMMAND % (EXAMPLE1a, EXAMPLE3a))
        self.sut.expect("Page 1 is different", timeout=2)
        assert self.sut.wait() == 2

    def test_different_1_page_docs_conmutative(self):
        self.sut = pexpect.spawn(COMMAND % (EXAMPLE3a, EXAMPLE1a))
        self.sut.expect("Page 1 is different", timeout=2)
        assert self.sut.wait() == 2

    def test_different_multipage_docs(self):
        self.sut = pexpect.spawn(COMMAND % (EXAMPLE2a, EXAMPLE4a))
        self.sut.expect("Page 4 is different", timeout=2)
        assert self.sut.wait() == 2
