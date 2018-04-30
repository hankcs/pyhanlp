# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_place_recognition(sentences):
    """ 地名识别

    >>> sentences = ["蓝翔给宁夏固原市彭阳县红河镇黑牛沟村捐赠了挖掘机"]
    >>> demo_place_recognition(sentences)
    [蓝翔/nt, 给/p, 宁夏/ns, 固原市/ns, 彭阳县/ns, 红河镇/ns, 黑牛沟村/ns, 捐赠/v, 了/ule, 挖掘机/n]
    """
    Segment = JClass("com.hankcs.hanlp.seg.Segment")
    Term = JClass("com.hankcs.hanlp.seg.common.Term")

    segment = HanLP.newSegment().enablePlaceRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
