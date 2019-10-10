# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-07 15:25
# 《自然语言处理入门》3.5.1 标准化评测
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.book.ch03.msr import msr_dict, msr_train, msr_model, msr_test, msr_output, msr_gold
from tests.book.ch03.ngram_segment import train_bigram, load_bigram

CWSEvaluator = SafeJClass('com.hankcs.hanlp.seg.common.CWSEvaluator')

if __name__ == '__main__':
    train_bigram(msr_train, msr_model)  # 训练
    segment = load_bigram(msr_model)  # 加载
    result = CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict)  # 预测打分
    print(result)
