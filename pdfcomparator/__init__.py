__version__ = (0, 1, 0)


class APP:
    version = __VERSION__
    name = 'pdfcomparator'
    description = 'Compares two PDF files by appearance, not by content.'

    @property
    def version_str(self):
        return ','.join(self.version)
