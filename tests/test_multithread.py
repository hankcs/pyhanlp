#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/pyhanlp/tests/test_multithread.py
# Author: Hai Liang Wang
# Date: 2018-03-23:17:18:30
#
#===============================================================================

"""
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2018-03-23:17:18:30"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

# Get ENV
ENVIRON = os.environ.copy()

from absl import flags   #absl-py
from absl import logging #absl-py

FLAGS = flags.FLAGS

import threading
import time
from pyhanlp import *

class MyThread (threading.Thread):
    def __init__(self, thread_id, name, counter, lock):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter
        self.lock = lock

    def run(self):
        print("Starting " + self.name)
        self.lock.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        self.lock.release()


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s, seg: %s" % (thread_name, time.ctime(time.time()), HanLP.segment("攻城狮逆袭单身狗，迎娶白富美，走上人生巅峰")))
        counter -= 1

import unittest

# run testcase: python /Users/hain/ai/pyhanlp/tests/test_multithread.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multithread(self):
        logging.info("test_multithread")

        threadLock = threading.Lock()

        thread1 = MyThread(1, "Thread-1", 1, threadLock)
        thread2 = MyThread(2, "Thread-2", 2, threadLock)

        thread1.start()
        thread2.start()

        print('waiting to finish the thread')

        thread1.join()
        thread2.join()

        print("Exiting Main Thread")

def test():
    unittest.main()

if __name__ == '__main__':
    FLAGS([__file__, '--verbosity', '1']) # DEBUG 1; INFO 0; WARNING -1
    test()
