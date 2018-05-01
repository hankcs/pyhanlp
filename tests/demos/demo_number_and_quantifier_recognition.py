# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_number_and_quantifier_recognition(sentences):
    """ 演示数词和数量词识别

    >>> sentences = [
    ...    "十九元套餐包括什么",
    ...    "九千九百九十九朵玫瑰",
    ...    "壹佰块都不给我",
    ...    "９０１２３４５６７８只蚂蚁",
    ...    "牛奶三〇〇克*2",
    ...    "ChinaJoy“扫黄”细则露胸超2厘米罚款",
    ... ]
    >>> demo_number_and_quantifier_recognition(sentences)
    [十九元/mq, 套餐/n, 包括/v, 什么/ry]
    [九千九百九十九朵/mq, 玫瑰/n]
    [壹佰块/mq, 都/d, 不/d, 给/p, 我/rr]
    [９０１２３４５６７８只/mq, 蚂蚁/n]
    [牛奶/nf, 三〇〇克/mq, */w, 2/m]
    [ChinaJoy/nx, “/w, 扫黄/vi, ”/w, 细则/n, 露/v, 胸/ng, 超/v, 2厘米/mq, 罚款/vi]
    """
    StandardTokenizer = JClass("com.hankcs.hanlp.tokenizer.StandardTokenizer")

    StandardTokenizer.SEGMENT.enableNumberQuantifierRecognize(True)
    for sentence in sentences:
        print(StandardTokenizer.segment(sentence))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
