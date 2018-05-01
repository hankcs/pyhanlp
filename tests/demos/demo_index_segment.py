# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-29
from pyhanlp import *
from jpype import *


def demo_index_segment():
    """ 索引分词

    >>> demo_index_segment()
    主副食品/n [0:4]
    主副食/j [0:3]
    副食品/n [1:4]
    副食/n [1:3]
    食品/n [2:4]
    最细颗粒度切分：
    主副食品/n [0:4]
    主副食/j [0:3]
    主/ag [0:1]
    副食品/n [1:4]
    副食/n [1:3]
    副/b [1:2]
    食品/n [2:4]
    食/v [2:3]
    品/ng [3:4]
    """
    Term =JClass("com.hankcs.hanlp.seg.common.Term")
    IndexTokenizer = JClass("com.hankcs.hanlp.tokenizer.IndexTokenizer")

    term_list = IndexTokenizer.segment("主副食品")
    for term in term_list.iterator():
        print("{} [{}:{}]".format(term, term.offset, term.offset + len(term.word)))

    print("最细颗粒度切分：")
    IndexTokenizer.SEGMENT.enableIndexMode(JInt(1))  # JInt用于区分重载
    term_list = IndexTokenizer.segment("主副食品")
    for term in term_list.iterator():
        print("{} [{}:{}]".format(term, term.offset, term.offset + len(term.word)))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
