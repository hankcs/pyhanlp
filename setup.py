# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-11 20:54
from os.path import abspath, join, dirname

from setuptools import find_packages, setup


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='pyhanlp',
    version='0.1.1',
    description='Python wrapper for HanLP: Han Language Processing',
    long_description=long_description,
    url='https://github.com/hankcs/pyhanlp',
    author='hankcs',
    author_email='hankcshe@gmail.com',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    keywords='Natural Language Processing',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=['jpype1'],
    entry_points={
        'console_scripts': [
            'hanlp=pyhanlp.main:main',
        ],
    },
)
