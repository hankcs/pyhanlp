# -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_use_AhoCorasickDoubleArrayTrieSegment():
    """ 基于AhoCorasickDoubleArrayTrie的分词器，该分词器允许用户跳过核心词典，直接使用自己的词典。
        需要注意的是，自己的词典必须遵守HanLP词典格式。

    >>> demo_use_AhoCorasickDoubleArrayTrieSegment()
    [微观经济学/nz, 继续教育/nz, 循环经济/nz]
    """
    AhoCorasickDoubleArrayTrieSegment = JClass(
        "com.hankcs.hanlp.seg.Other.AhoCorasickDoubleArrayTrieSegment")
    Config = JClass("com.hankcs.hanlp.HanLP$Config")

    # AhoCorasickDoubleArrayTrieSegment要求用户必须提供自己的词典路径
    segment = AhoCorasickDoubleArrayTrieSegment(
        ).loadDictionary(Config.CustomDictionaryPath[0])
    print(segment.seg("微观经济学继续教育循环经济"))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
