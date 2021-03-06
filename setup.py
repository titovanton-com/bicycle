#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages

import bicycle


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


def without_mainapp(item):
    return not bool(item.find('mainapp') + 1)

packages = filter(without_mainapp, find_packages())

setup(name="bicycle",
      version=bicycle.__version__,
      description="My helpers.",
      long_description=read("README.rst"),
      author="Titov Anton",
      author_email="mail@titovanton.com",
      license="BSD",
      url="https://github.com/titovanton-com/bicycle",
      packages=packages,
      zip_safe=False)
