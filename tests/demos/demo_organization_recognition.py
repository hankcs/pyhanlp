# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_organization_recognition(sentences):
    """ 机构名识别

    >>> sentences = [
    ...    "我在上海林原科技有限公司兼职工作，",
    ...    "我经常在台川喜宴餐厅吃饭，",
    ...    "偶尔去开元地中海影城看电影。",
    ... ]
    >>> demo_organization_recognition(sentences)
    [我/rr, 在/p, 上海/ns, 林原科技有限公司/nt, 兼职/vn, 工作/vn, ，/w]
    [我/rr, 经常/d, 在/p, 台川喜宴餐厅/nt, 吃饭/vi, ，/w]
    [偶尔/d, 去/vf, 开元地中海影城/nt, 看/v, 电影/n, 。/w]
    """
    Segment = JClass("com.hankcs.hanlp.seg.Segment")
    Term = JClass("com.hankcs.hanlp.seg.common.Term")

    segment = HanLP.newSegment().enableOrganizationRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
