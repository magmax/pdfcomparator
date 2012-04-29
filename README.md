PDF Comparator
==========

Compares two PDF files by appearance, not by content. It can be used in the command line, in order to use it inside bigger scripts.

Usage
----------

The format is the next one:

	:::
		$ pdfcompare.py pattern current

It will compare the files under "pattern" and "current".

If they are equal, it will print nothing. If they are different, it will print the first page that is different and the script will return 2.

Enjoy it!
