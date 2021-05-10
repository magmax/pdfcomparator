FROM python:3.9.5-buster

RUN apt-get -y update \
    && apt-get install -y \
        libpoppler-glib-dev \
        libpoppler-cpp-dev \
        python-gobject \
        build-essential \
        cmake
RUN pip install python-poppler

COPY pdfcomparator/pdfcompare.py .

ENTRYPOINT["/pdfcompare.py"]
