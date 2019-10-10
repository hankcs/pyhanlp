# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-05 10:19
# 《自然语言处理入门》7.3.2 基于感知机的词性标注
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from pyhanlp import *
from tests.book.ch07.demo_hmm_pos import AbstractLexicalAnalyzer, PerceptronSegmenter
from tests.book.ch07.pku import PKU199801_TRAIN, POS_MODEL

POSTrainer = JClass('com.hankcs.hanlp.model.perceptron.POSTrainer')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')


def train_perceptron_pos(corpus):
    trainer = POSTrainer()
    trainer.train(corpus, POS_MODEL)  # 训练
    tagger = PerceptronPOSTagger(POS_MODEL)  # 加载
    print(', '.join(tagger.tag("他", "的", "希望", "是", "希望", "上学")))  # 预测
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), tagger)  # 构造词法分析器
    print(analyzer.analyze("李狗蛋的希望是希望上学"))  # 分词+词性标注
    return tagger


if __name__ == '__main__':
    train_perceptron_pos(PKU199801_TRAIN)
