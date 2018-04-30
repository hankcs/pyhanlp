# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_pos_tagging():
    """ 词性标注

    >>> demo_pos_tagging()
    未标注： [教授/nnt, 正在/d, 教授/nnt, 自然语言处理/nz, 课程/n]
    标注后： [教授/nnt, 正在/d, 教授/v, 自然语言处理/nz, 课程/n]
    """
    Segment = JClass("com.hankcs.hanlp.seg.Segment")
    text = "教授正在教授自然语言处理课程"
    segment = HanLP.newSegment()

    print("未标注：", segment.seg(text))
    segment.enablePartOfSpeechTagging(True)
    print("标注后：", segment.seg(text))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
