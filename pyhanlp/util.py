#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/pyhanlp/pyhanlp/util.py
# Author: Hai Liang Wang
# Date: 2018-03-19:19:14:56
#
#===============================================================================

"""
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2018-03-19:19:14:56"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, os.path.pardir))

PY = 3
if sys.version_info[0] < 3:
    PY = 2
    # noinspection PyUnresolvedReferences
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

# Get ENV
ENVIRON = os.environ.copy()

try:
    from html.entities import name2codepoint as n2cp
except ImportError:
    # noinspection PyUnresolvedReferences
    from htmlentitydefs import name2codepoint as n2cp
try:
    import cPickle as _pickle
except ImportError:
    import pickle as _pickle

try:
    from smart_open import smart_open
except ImportError:
    # print("smart_open library not found; falling back to local-filesystem-only")

    def make_closing(base, **attrs):
        """
        Add support for `with Base(attrs) as fout:` to the base class if it's missing.
        The base class' `close()` method will be called on context exit, to always close the file properly.

        This is needed for gzip.GzipFile, bz2.BZ2File etc in older Pythons (<=2.6), which otherwise
        raise "AttributeError: GzipFile instance has no attribute '__exit__'".

        """
        if not hasattr(base, '__enter__'):
            attrs['__enter__'] = lambda self: self
        if not hasattr(base, '__exit__'):
            attrs['__exit__'] = lambda self, type, value, traceback: self.close()
        return type('Closing' + base.__name__, (base, object), attrs)

    def smart_open(fname, mode='rb'):
        _, ext = os.path.splitext(fname)
        if ext == '.bz2':
            from bz2 import BZ2File
            return make_closing(BZ2File)(fname, mode)
        if ext == '.gz':
            from gzip import GzipFile
            return make_closing(GzipFile)(fname, mode)
        return open(fname, mode)


# noinspection PyUnresolvedReferences
def any2utf8(text, errors='strict', encoding='utf8'):
    if PY == 3:
        return text
    """Convert a string (unicode or bytestring in `encoding`), to bytestring in utf8."""
    if isinstance(text, unicode):
        return text.encode('utf8')
    # do bytestring -> unicode -> utf8 full circle, to ensure valid utf8
    return unicode(text, encoding, errors=errors).encode('utf8')


to_utf8 = any2utf8

# noinspection PyUnresolvedReferences
def any2unicode(text, encoding='utf8', errors='strict'):
    """Convert a string (bytestring in `encoding` or unicode), to unicode."""
    if isinstance(text, unicode):
        return text
    return unicode(text, encoding, errors=errors)


to_unicode = any2unicode
