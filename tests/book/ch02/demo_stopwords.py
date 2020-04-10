# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-04 11:17
# 《自然语言处理入门》2.10.1 停用词过滤
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from jpype import JString

from pyhanlp import *


def load_from_file(path):
    """
    从词典文件加载DoubleArrayTrie
    :param path: 词典路径
    :return: 双数组trie树
    """
    map = JClass('java.util.TreeMap')()  # 创建TreeMap实例
    with open(path, encoding='utf-8') as src:
        for word in src:
            word = word.strip()  # 去掉Python读入的\n
            map[word] = word
    return JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')(map)


def load_from_words(*words):
    """
    从词汇构造双数组trie树
    :param words: 一系列词语
    :return:
    """
    map = JClass('java.util.TreeMap')()  # 创建TreeMap实例
    for word in words:
        map[word] = word
    return JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')(map)


def remove_stopwords_termlist(termlist, trie):
    return [term.word for term in termlist if not trie.containsKey(term.word)]


def replace_stropwords_text(text, replacement, trie):
    searcher = trie.getLongestSearcher(JString(text), 0)
    offset = 0
    result = ''
    while searcher.next():
        begin = searcher.begin
        end = begin + searcher.length
        if begin > offset:
            result += text[offset: begin]
        result += replacement
        offset = end
    if offset < len(text):
        result += text[offset:]
    return result


if __name__ == '__main__':
    HanLP.Config.ShowTermNature = False
    trie = load_from_file(HanLP.Config.CoreStopWordDictionaryPath)
    text = "停用词的意义相对而言无关紧要吧。"
    segment = DoubleArrayTrieSegment()
    termlist = segment.seg(text)
    print("分词结果：", termlist)
    print("分词结果去除停用词：", remove_stopwords_termlist(termlist, trie))
    trie = load_from_words("的", "相对而言", "吧")
    print("不分词去掉停用词", replace_stropwords_text(text, "**", trie))
