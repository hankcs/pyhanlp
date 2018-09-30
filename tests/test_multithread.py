#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/pyhanlp/tests/test_multithread.py
# Author: Hai Liang Wang
# Date: 2018-03-23:17:18:30
#
# ===============================================================================
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2018-03-23:17:18:30"

import os
import sys

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, os.path.pardir))

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

from absl import flags  # absl-py
from absl import logging  # absl-py

FLAGS = flags.FLAGS
import unittest
import threading
import time
from pyhanlp import HanLP, SafeJClass

# 在线程体外部用SafeJClass线程安全地引入类名
CRFLexicalAnalyzer = SafeJClass("com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer")


class MyThread(threading.Thread):
    def __init__(self, name, counter, analyzer):
        threading.Thread.__init__(self)
        self.thread_name = name
        self.counter = counter
        self.analyzer = analyzer

    def run(self):
        print("Starting " + self.thread_name)
        while self.counter:
            time.sleep(1)
            sentence = self.analyzer.analyze("商品和服务")
            print("%s: %s, seg: %s" % (self.thread_name, time.ctime(time.time()), sentence))
            self.counter -= 1


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multithread(self):
        logging.info("test_multithread")
        # 在线程外部创建对象，供多个线程共用
        analyzer = CRFLexicalAnalyzer()

        thread1 = MyThread("Thread-1", 1, analyzer)
        thread2 = MyThread("Thread-2", 2, analyzer)

        thread1.start()
        thread2.start()

        print('waiting to finish the thread')

        thread1.join()
        thread2.join()

        print("Exiting Main Thread")


def test():
    unittest.main()


if __name__ == '__main__':
    FLAGS([__file__, '--verbosity', '1'])  # DEBUG 1; INFO 0; WARNING -1
    test()
