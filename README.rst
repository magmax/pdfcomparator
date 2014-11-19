==============  ===============  =========  ============
VERSION         DOWNLOADS        TESTS      COVERAGE
==============  ===============  =========  ============
|pip version|   |pip downloads|  |travis|   |coveralls|
==============  ===============  =========  ============

Compares two PDF files by appearance, not by content. It can be used in the command line, in order to use it inside bigger scripts.

Installation
------------

It requires some libraries. In Debian or Ubuntu, you can install them by apt::

    # apt-get install libpoppler-glib-dev python-gtk2 python-cairo-dev python-gobject-dev

Then you can install it as usual::

    $ pip install pdfcomparator

Usage
-----

The format is the next one:

    $ pdfcompare.py pattern current

It will compare the files under "pattern" and "current".

If they are equal, it will print nothing. If they are different, it will print the first page that is different and the script will return 2.

Enjoy it!


Contribute
----------

If you want to contribute, please, create a VirtualEnv environment::

    $ virtualenv venv --system-site-packages
    $ . venv/bin/activate

It is important to use the system packages in order to find the python-gobject library.

Now, you should be able to install the pdfcomparator package:

    $ python setup.py develop

And to test it:

    $ python setup.py test


.. |travis| image:: https://travis-ci.org/magmax/pdfcomparator.png
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://coveralls.io/repos/magmax/pdfcomparator/badge.png
  :target: `Coveralls`_
  :alt: Coveralls results_

.. |pip version| image:: https://pypip.in/v/pdfcomparator/badge.png
    :target: https://pypi.python.org/pypi/pdfcomparator
    :alt: Latest PyPI version

.. |pip downloads| image:: https://pypip.in/d/pdfcomparator/badge.png
    :target: https://pypi.python.org/pypi/pdfcomparator
    :alt: Number of PyPI downloads

.. _Travis: https://travis-ci.org/magmax/pdfcomparator
.. _Coveralls: https://coveralls.io/r/magmax/pdfcomparator
