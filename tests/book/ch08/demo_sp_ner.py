# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-29 15:06
# 《自然语言处理入门》8.5.3 基于感知机序列标注的命名实体识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.book.ch07 import pku
from tests.book.ch08.demo_hmm_ner import test, PerceptronSegmenter, PerceptronPOSTagger
from tests.book.ch08.demo_role_tag_nr import Sentence

NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
PerceptronNERecognizer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronNERecognizer')


def train(corpus, model):
    trainer = NERTrainer()
    return PerceptronNERecognizer(trainer.train(corpus, model).getModel())


if __name__ == '__main__':
    recognizer = train(pku.PKU199801_TRAIN, pku.NER_MODEL)
    test(recognizer)
    analyzer = PerceptronLexicalAnalyzer(PerceptronSegmenter(), PerceptronPOSTagger(), recognizer)  # ①
    analyzer.enableCustomDictionary(False)
    sentence = Sentence.create("与/c 特朗普/nr 通/v 电话/n 讨论/v [太空/s 探索/vn 技术/n 公司/n]/nt")  # ②
    while not analyzer.analyze(sentence.text()).equals(sentence):  # ③
        analyzer.learn(sentence)
