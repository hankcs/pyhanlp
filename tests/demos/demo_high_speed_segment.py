# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-29
from pyhanlp import *
import time


def demo_high_speed_segment():
    """ 演示极速分词，基于DoubleArrayTrie实现的词典正向最长分词，适用于“高吞吐量”“精度一般”的场合

    >>> demo_high_speed_segment()
    [江西, 鄱阳湖, 干枯, ，, 中国, 最大, 淡水湖, 变成, 大草原]
    SpeedTokenizer分词速度：1253607.32字每秒
    """
    SpeedTokenizer = JClass("com.hankcs.hanlp.tokenizer.SpeedTokenizer")
    text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原"
    JClass("com.hankcs.hanlp.HanLP$Config").ShowTermNature = False
    print(SpeedTokenizer.segment(text))

    start = time.time()
    pressure = 1000000
    for i in range(pressure):
        SpeedTokenizer.segment(text)
    cost_time = time.time() - start
    print("SpeedTokenizer分词速度：%.2f字每秒" % (len(text) * pressure / cost_time))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
