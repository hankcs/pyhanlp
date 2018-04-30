# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_pinyin_to_chinese():
    """ HanLP中的数据结构和接口是灵活的，组合这些接口，可以自己创造新功能

    >>> demo_pinyin_to_chinese()
    [renmenrenweiyalujiangbujian/null, lvse/[滤色, 绿色]]
    """
    AhoCorasickDoubleArrayTrie = JClass(
        "com.hankcs.hanlp.collection.AhoCorasick.AhoCorasickDoubleArrayTrie")
    StringDictionary = JClass(
        "com.hankcs.hanlp.corpus.dictionary.StringDictionary")
    CommonAhoCorasickDoubleArrayTrieSegment = JClass(
        "com.hankcs.hanlp.seg.Other.CommonAhoCorasickDoubleArrayTrieSegment")
    CommonAhoCorasickSegmentUtil = JClass(
        "com.hankcs.hanlp.seg.Other.CommonAhoCorasickSegmentUtil")
    Config = JClass("com.hankcs.hanlp.HanLP$Config")

    TreeMap = JClass("java.util.TreeMap")
    TreeSet = JClass("java.util.TreeSet")

    dictionary = StringDictionary()
    dictionary.load(Config.PinyinDictionaryPath)
    entry = {}
    m_map = TreeMap()
    for entry in dictionary.entrySet():
        pinyins = entry.getValue().replace("[\\d,]", "")
        words = m_map.get(pinyins)
        if words is None:
            words = TreeSet()
            m_map.put(pinyins, words)
        words.add(entry.getKey())
    words = TreeSet()
    words.add("绿色")
    words.add("滤色")
    m_map.put("lvse", words)

    segment = CommonAhoCorasickDoubleArrayTrieSegment(m_map)
    print(segment.segment("renmenrenweiyalujiangbujianlvse"))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
