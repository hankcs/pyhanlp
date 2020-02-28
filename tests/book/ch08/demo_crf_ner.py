# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-29 18:07
# 《自然语言处理入门》8.5.4 基于条件随机场序列标注的命名 实体识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.book.ch07 import pku
from tests.book.ch08.demo_hmm_ner import test

NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
CRFNERecognizer = JClass('com.hankcs.hanlp.model.crf.CRFNERecognizer')


def train(corpus, model):
    recognizer = CRFNERecognizer(None)  # 空白
    recognizer.train(corpus, model)
    recognizer = CRFNERecognizer(model)
    return recognizer


if __name__ == '__main__':
    recognizer = train(pku.PKU199801_TRAIN, pku.NER_MODEL)
    test(recognizer)
