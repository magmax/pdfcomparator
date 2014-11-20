# -*- coding: utf-8 -*-

import subprocess
from setuptools import setup, find_packages, Command
from pdfcomparator import APP


def read_description():
    with open('README.rst') as fd:
        return fd.read()


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py', 'tests'])
        raise SystemExit(errno)


setup(name=APP.name,
      version=APP.version_str,
      description=APP.description,
      long_description=read_description(),
      cmdclass = {'test': PyTest},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      keywords='pdf comparator',
      author='Miguel Ángel García',
      author_email='miguelangel.garcia@gmail.com',
      url='https://github.com/magmax/pdfcomparator',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
#          'pygobject',
          'pypoppler',
          'pycairo == 1.8.8',
      ],
      tests_require=[
          'flake8 >= 2.2.3',
          'pytest >= 2.6.3',
          'pytest-cov >= 1.8.0',
          'pexpect >= 3.3',
          'wheel >= 0.24.0',
          'python-coveralls >= 2.4.2',
      ],
  )
