# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-21 19:46
# 《自然语言处理入门》5.3 基于感知机的人名性别分类
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from pyhanlp import *
from tests.test_utility import ensure_data

PerceptronNameGenderClassifier = JClass('com.hankcs.hanlp.model.perceptron.PerceptronNameGenderClassifier')
cnname = ensure_data('cnname', 'http://file.hankcs.com/corpus/cnname.zip')
TRAINING_SET = os.path.join(cnname, 'train.csv')
TESTING_SET = os.path.join(cnname, 'test.csv')
MODEL = cnname + ".bin"


def run_classifier(averaged_perceptron):
    print('=====%s=====' % ('平均感知机算法' if averaged_perceptron else '朴素感知机算法'))
    classifier = PerceptronNameGenderClassifier()
    print('训练集准确率：', classifier.train(TRAINING_SET, 10, averaged_perceptron))
    model = classifier.getModel()
    print('特征数量：', len(model.parameter))
    # model.save(MODEL, model.featureMap.entrySet(), 0, True)
    # classifier = PerceptronNameGenderClassifier(MODEL)
    for name in "赵建军", "沈雁冰", "陆雪琪", "李冰冰":
        print('%s=%s' % (name, classifier.predict(name)))
    print('测试集准确率：', classifier.evaluate(TESTING_SET))


if __name__ == '__main__':
    run_classifier(False)
    run_classifier(True)
