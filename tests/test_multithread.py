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
__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2018-03-23:17:18:30"

import threading
import time

import pytest

from pyhanlp import SafeJClass


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


@pytest.fixture()
def analyzer():
    # 在线程体外部用SafeJClass线程安全地引入类名
    CRFLexicalAnalyzer = SafeJClass("com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer")
    # 在线程外部创建对象，供多个线程共用
    analyzer = CRFLexicalAnalyzer()
    return analyzer


@pytest.fixture()
def thread1():
    return MyThread("Thread-1", 1, analyzer)


@pytest.fixture()
def thread2():
    return MyThread("Thread-2", 2, analyzer)


def test_sth(thread1, thread2):
    thread1.start()
    thread2.start()

    print('waiting to finish the thread')

    thread1.join(timeout=3)
    thread2.join(timeout=3)

    print("Exiting Main Thread")
