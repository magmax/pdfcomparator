__version__ = (0, 1, 0)


class APP:
    version = __version__
    name = 'pdfcomparator'
    description = 'Compares two PDF files by appearance, not by content.'

    version_str = str.join(',', (str(x) for x in version))
