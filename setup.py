#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages

def get_version():
    here = os.path.dirname(__file__)
    init_file = os.path.join(here, 'freekey', 'main.py')
    with open(init_file, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r"^__version__\s*=\s*['\"]([^'\"]+)['\"]", content, re.M)
    return m.group(1) if m else '0.0.0'

setup(
    name='freekey',
    version=get_version(),
    description='Allows limited keyboard use on a locked desktop',
    author='Chris Spencer',
    author_email='chrisspen@gmail.com',
    url='https://github.com/chrisspen/freekey',
    license='LGPL',
    packages=find_packages(),
    #install_requires=[],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        'console_scripts': [
            'freekey=freekey.main:main',
        ],
    },
    platforms=['Linux']
)
