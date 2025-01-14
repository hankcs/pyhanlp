# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-11 20:54
from os.path import abspath, join, dirname
import sys
from setuptools import find_packages, setup

JPYPE = 'jpype1>=1.5.0' if sys.version_info >= (3, 8) else 'jpype1==0.7.0'

if sys.version_info[0] < 3:  # In Python3 TypeError: a bytes-like object is required, not 'str'
    long_description = 'Python wrapper for HanLP: Han Language Processing'
else:
    this_dir = abspath(dirname(__file__))
    with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
        long_description = file.read()

setup(
    name='pyhanlp',
    version='0.1.87',
    description='Python wrapper for HanLP: Han Language Processing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hankcs/pyhanlp',
    author='hankcs',
    author_email='hankcshe@gmail.com',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic'
    ],
    keywords='corpus,machine-learning,NLU,NLP',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=[JPYPE, 'hanlp-downloader'],
    entry_points={
        'console_scripts': [
            'hanlp=pyhanlp.main:main',
        ],
    },
    # python_requires='<3.9',
)
