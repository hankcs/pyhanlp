# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-02-26 22:58
# 《自然语言处理入门》13.4 基于神经网络的高性能依存句法分析器
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *

CoNLLSentence = JClass('com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLSentence')
CoNLLWord = JClass('com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLWord')
IDependencyParser = JClass('com.hankcs.hanlp.dependency.IDependencyParser')
NeuralNetworkDependencyParser = JClass('com.hankcs.hanlp.dependency.nnparser.NeuralNetworkDependencyParser')

if __name__ == '__main__':
    parser = NeuralNetworkDependencyParser()
    sentence = parser.parse("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。")
    print(sentence)
    for word in sentence.iterator():  # 通过dir()可以查看sentence的方法
        print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
    print()

    # 也可以直接拿到数组，任意顺序或逆序遍历
    word_array = sentence.getWordArray()
    for word in word_array:
        print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
    print()

    # 还可以直接遍历子树，从某棵子树的某个节点一路遍历到虚根
    CoNLLWord = JClass("com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLWord")
    head = word_array[12]
    while head.HEAD:
        head = head.HEAD
        if (head == CoNLLWord.ROOT):
            print(head.LEMMA)
        else:
            print("%s --(%s)--> " % (head.LEMMA, head.DEPREL))
