# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-06-02 18:03
# 《自然语言处理入门》12.6 案例:基于依存句法树的意见抽取
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from pyhanlp import *

CoNLLSentence = JClass('com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLSentence')
CoNLLWord = JClass('com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLWord')
IDependencyParser = JClass('com.hankcs.hanlp.dependency.IDependencyParser')
KBeamArcEagerDependencyParser = JClass('com.hankcs.hanlp.dependency.perceptron.parser.KBeamArcEagerDependencyParser')


def main():
    parser = KBeamArcEagerDependencyParser()
    tree = parser.parse("电池非常棒，机身不长，长的是待机，但是屏幕分辨率不高。")
    print(tree)
    print("第一版")
    extactOpinion1(tree)
    print("第二版")
    extactOpinion2(tree)
    print("第三版")
    extactOpinion3(tree)


def extactOpinion1(tree):
    for word in tree.iterator():
        if word.POSTAG == "NN" and word.DEPREL == "nsubj":
            print("%s = %s" % (word.LEMMA, word.HEAD.LEMMA))


def extactOpinion2(tree):
    for word in tree.iterator():
        if word.POSTAG == "NN" and word.DEPREL == "nsubj":
            if tree.findChildren(word.HEAD, "neg").isEmpty():
                print("%s = %s" % (word.LEMMA, word.HEAD.LEMMA))
            else:
                print("%s = 不%s" % (word.LEMMA, word.HEAD.LEMMA))


def extactOpinion3(tree):
    for word in tree.iterator():
        if word.POSTAG == "NN":
            if word.DEPREL == "nsubj":  # ①属性

                if tree.findChildren(word.HEAD, "neg").isEmpty():
                    print("%s = %s" % (word.LEMMA, word.HEAD.LEMMA))
                else:
                    print("%s = 不%s" % (word.LEMMA, word.HEAD.LEMMA))
            elif word.DEPREL == "attr":
                top = tree.findChildren(word.HEAD, "top")  # ②主题

                if not top.isEmpty():
                    print("%s = %s" % (word.LEMMA, top.get(0).LEMMA))


if __name__ == '__main__':
    main()
