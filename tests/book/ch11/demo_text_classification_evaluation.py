# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-01-04 20:28
# 《自然语言处理入门》11.6 标准化评测
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.demos.demo_text_classification import sogou_corpus_path

IClassifier = JClass('com.hankcs.hanlp.classification.classifiers.IClassifier')
NaiveBayesClassifier = JClass('com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier')
LinearSVMClassifier = JClass('com.hankcs.hanlp.classification.classifiers.LinearSVMClassifier')
FileDataSet = JClass('com.hankcs.hanlp.classification.corpus.FileDataSet')
IDataSet = JClass('com.hankcs.hanlp.classification.corpus.IDataSet')
MemoryDataSet = JClass('com.hankcs.hanlp.classification.corpus.MemoryDataSet')
Evaluator = JClass('com.hankcs.hanlp.classification.statistics.evaluations.Evaluator')
FMeasure = JClass('com.hankcs.hanlp.classification.statistics.evaluations.FMeasure')
BigramTokenizer = JClass('com.hankcs.hanlp.classification.tokenizers.BigramTokenizer')
HanLPTokenizer = JClass('com.hankcs.hanlp.classification.tokenizers.HanLPTokenizer')
ITokenizer = JClass('com.hankcs.hanlp.classification.tokenizers.ITokenizer')


def evaluate(classifier, tokenizer):
    training_corpus = FileDataSet().setTokenizer(tokenizer).load(sogou_corpus_path, "UTF-8", 0.9)
    classifier.train(training_corpus)
    testing_corpus = MemoryDataSet(classifier.getModel()).load(sogou_corpus_path, "UTF-8", -0.1)
    result = Evaluator.evaluate(classifier, testing_corpus)
    print(classifier.getClass().getSimpleName() + "+" + tokenizer.getClass().getSimpleName())
    print(result)


if __name__ == '__main__':
    evaluate(NaiveBayesClassifier(), HanLPTokenizer())
    evaluate(NaiveBayesClassifier(), BigramTokenizer())
    evaluate(LinearSVMClassifier(), HanLPTokenizer())
    evaluate(LinearSVMClassifier(), BigramTokenizer())
