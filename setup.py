#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'gogplot',
    version = '0.0.1',
    author = 'Leon du Toit',
    author_email = 'dutoit.leon@gmail.com',
    packages = ['gogplot'],
    url = 'https://github.com/leondutoit/gogplot',
    license = 'LICENSE',
    description = 'Use R\'s ggplot2 from python with pandas',
    long_description = open('README.md').read(),
    install_requires = [
        "pandas = 0.13.0"
    ],
)
