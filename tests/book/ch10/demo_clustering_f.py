# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-08-19 20:01
# 《自然语言处理入门》10.5 标准化评测
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.demos.demo_text_classification import sogou_corpus_path

ClusterAnalyzer = JClass('com.hankcs.hanlp.mining.cluster.ClusterAnalyzer')

if __name__ == '__main__':
    for algorithm in "kmeans", "repeated bisection":
        print("%s F1=%.2f\n" % (algorithm, ClusterAnalyzer.evaluate(sogou_corpus_path, algorithm) * 100))
