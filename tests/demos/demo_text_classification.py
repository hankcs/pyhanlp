# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-23 17:26
import os

from pyhanlp import SafeJClass
from tests.test_utility import ensure_data

NaiveBayesClassifier = SafeJClass('com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier')
IOUtil = SafeJClass('com.hankcs.hanlp.corpus.io.IOUtil')
sogou_corpus_path = ensure_data('搜狗文本分类语料库迷你版',
                                'http://hanlp.linrunsoft.com/release/corpus/sogou-text-classification-corpus-mini.zip')


def train_or_load_classifier():
    model_path = sogou_corpus_path + '.ser'
    if os.path.isfile(model_path):
        return NaiveBayesClassifier(IOUtil.readObjectFrom(model_path))
    classifier = NaiveBayesClassifier()
    classifier.train(sogou_corpus_path)
    model = classifier.getModel()
    IOUtil.saveObjectTo(model, model_path)
    return NaiveBayesClassifier(model)


def predict(classifier, text):
    print("《%16s》\t属于分类\t【%s】" % (text, classifier.predict(text)))


if __name__ == '__main__':
    classifier = train_or_load_classifier()
    predict(classifier, "C罗压梅西内马尔蝉联金球奖 2017=C罗年")
    predict(classifier, "英国造航母耗时8年仍未服役 被中国速度远远甩在身后")
    predict(classifier, "研究生考录模式亟待进一步专业化")
    predict(classifier, "如果真想用食物解压,建议可以食用燕麦")
    predict(classifier, "通用及其部分竞争对手目前正在考虑解决库存问题")
