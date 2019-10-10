# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-28 20:59
# 《自然语言处理入门》8.5.2 基于隐马尔可夫模型序列标注的 命名实体识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.book.ch07 import pku

HMMNERecognizer = JClass('com.hankcs.hanlp.model.hmm.HMMNERecognizer')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')
Utility = JClass('com.hankcs.hanlp.model.perceptron.utility.Utility')


def train(corpus):
    recognizer = HMMNERecognizer()
    recognizer.train(corpus)  # data/test/pku98/199801-train.txt
    return recognizer


def test(recognizer):
    word_array = ["华北", "电力", "公司"]  # 构造单词序列
    pos_array = ["ns", "n", "n"]  # 构造词性序列
    ner_array = recognizer.recognize(word_array, pos_array)  # 序列标注
    for word, tag, ner in zip(word_array, pos_array, ner_array):
        print("%s\t%s\t%s\t" % (word, tag, ner))
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), PerceptronPOSTagger(), recognizer)
    print(analyzer.analyze("华北电力公司董事长谭旭光和秘书胡花蕊来到美国纽约现代艺术博物馆参观"))
    scores = Utility.evaluateNER(recognizer, pku.PKU199801_TEST)
    Utility.printNERScore(scores)


if __name__ == '__main__':
    recognizer = train(pku.PKU199801_TRAIN)
    test(recognizer)
