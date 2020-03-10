# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-22 15:18
# 《自然语言处理入门》5.6 基于结构化感知机的中文分词
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.book.ch03.eval_bigram_cws import CWSEvaluator
from tests.book.ch03.msr import msr_train, msr_model, msr_dict, msr_gold, msr_output, msr_test

CWSTrainer = JClass('com.hankcs.hanlp.model.perceptron.CWSTrainer')


def train_uncompressed_model():
    model = CWSTrainer().train(msr_train, msr_train, msr_model, 0., 10, 8).getModel()  # 训练模型
    model.save(msr_model, model.featureMap.entrySet(), 0, True)  # 最后一个参数指定导出txt


def train():
    model = CWSTrainer().train(msr_train, msr_model).getModel()  # 训练模型
    segment = PerceptronLexicalAnalyzer(model).enableCustomDictionary(False)  # 创建分词器
    return segment
    # print(CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict))  # 标准化评测


if __name__ == '__main__':
    segment = train()
    sents = [
        "王思斌，男，１９４９年１０月生。",
        "山东桓台县起凤镇穆寨村妇女穆玲英",
        "现为中国艺术研究院中国文化研究所研究员。",
        "我们的父母重男轻女",
        "北京输气管道工程",
    ]
    for sent in sents:
        print(segment.seg(sent))
    # train_uncompressed_model()
