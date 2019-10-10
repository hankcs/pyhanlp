# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-28 15:22
# 《自然语言处理入门》2.6 AC 自动机
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *


def classic_demo():
    words = ["hers", "his", "she", "he"]
    Trie = JClass('com.hankcs.hanlp.algorithm.ahocorasick.trie.Trie')
    trie = Trie()
    for w in words:
        trie.addKeyword(w)

    for emit in trie.parseText("ushers"):
        print("[%d:%d]=%s" % (emit.getStart(), emit.getEnd(), emit.getKeyword()))


if __name__ == '__main__':
    classic_demo()
