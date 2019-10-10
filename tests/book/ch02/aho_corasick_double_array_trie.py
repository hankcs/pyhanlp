# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-28 18:10
# 《自然语言处理入门》2.7 基于双数组字典树的 AC 自动机
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from pyhanlp import *


def classic_demo():
    words = ["hers", "his", "she", "he"]
    map = JClass('java.util.TreeMap')()     # 创建TreeMap实例
    for word in words:
        map[word] = word.upper()            # 存放键值对
    trie = JClass('com.hankcs.hanlp.collection.AhoCorasick.AhoCorasickDoubleArrayTrie')(map)
    for hit in trie.parseText("ushers"):    # 遍历查询结果
        print("[%d:%d]=%s" % (hit.begin, hit.end, hit.value))


if __name__ == '__main__':
    classic_demo()