# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-22 17:53
# 《自然语言处理入门》5.6.3 特征裁剪与模型压缩
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
import os

import matplotlib.pyplot as plt
from jpype import JClass

from tests.book.ch03.eval_bigram_cws import CWSEvaluator
from tests.book.ch03.msr import msr_train, msr_model, msr_gold, msr_dict, msr_output, msr_test
from tests.book.ch05.perceptron_cws import CWSTrainer, PerceptronLexicalAnalyzer

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def train_evaluate(ratios):
    if not os.path.isfile(msr_model):
        model = CWSTrainer().train(msr_train, msr_train, msr_model, 0, 10, 8).getModel()  # 训练模型
    else:
        model = JClass('com.hankcs.hanlp.model.perceptron.model.LinearModel')(msr_model)
    pre = None
    scores = []
    for c in ratios:
        if pre:
            print('以压缩比{}压缩模型中...'.format(c))
            model.compress(1 - (1 - c) / pre, 0)
        pre = 1 - c
        result = CWSEvaluator.evaluate(PerceptronLexicalAnalyzer(model).enableCustomDictionary(False),
                                       msr_test, msr_output, msr_gold, msr_dict)
        # scores.append(result.F1)
        scores.append(float(str(result).split()[2][3:]))
    return scores


if __name__ == '__main__':
    x = [c / 10 for c in range(0, 10)]
    y = train_evaluate(x)
    plt.title("压缩率对准确率的影响")
    plt.xlabel("压缩率")
    plt.ylabel("准确率")
    plt.xticks([c / 10 for c in range(0, 11)])
    # plt.ylim(min(y), max(y))
    plt.plot(x, y, color='b')
    plt.grid()
    plt.show()
