# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-24 22:04
# 《自然语言处理入门》8.4.1 基于角色标注的中国人名识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.book.ch03.ngram_segment import DijkstraSegment
from tests.book.ch07 import pku
from tests.test_utility import test_data_path

EasyDictionary = JClass('com.hankcs.hanlp.corpus.dictionary.EasyDictionary')
NRDictionaryMaker = JClass('com.hankcs.hanlp.corpus.dictionary.NRDictionaryMaker')
Sentence = JClass('com.hankcs.hanlp.corpus.document.sentence.Sentence')
MODEL = test_data_path() + "/nr"


def demoNR():
    HanLP.Config.enableDebug()
    segment = DijkstraSegment()
    print(segment.seg("王国维和服务员"))


def train_one_sent():
    dictionary = EasyDictionary.create(HanLP.Config.CoreDictionaryPath)  # 核心词典
    maker = NRDictionaryMaker(dictionary)  # 训练模块
    maker.verbose = True  # 调试输出
    maker.learn([Sentence.create("这里/r 有/v 关天培/nr 的/u 有关/vn 事迹/n 。/w")])  # 学习一个句子
    maker.saveTxtTo(MODEL)  # 输出HMM到txt


def train(corpus, model):
    dictionary = EasyDictionary.create(HanLP.Config.CoreDictionaryPath)  # 核心词典
    maker = NRDictionaryMaker(dictionary)  # 训练模块
    maker.train(corpus)  # 在语料库上训练
    maker.saveTxtTo(model)  # 输出HMM到txt


def load(model):
    HanLP.Config.PersonDictionaryPath = model + ".txt"  # data/test/nr.txt
    HanLP.Config.PersonDictionaryTrPath = model + ".tr.txt"  # data/test/nr.tr.txt
    segment = DijkstraSegment()  # 该分词器便于调试
    return segment


def test():
    segment = load(MODEL)
    HanLP.Config.enableDebug()
    print(segment.seg("龚学平等领导"))


if __name__ == '__main__':
    demoNR()
    train_one_sent()
    train(pku.PKU199801, MODEL)
    test()
