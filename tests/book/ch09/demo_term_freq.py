# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-08-01 16:15
# 《自然语言处理入门》9.2 关键词提取
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *

TermFrequency = JClass('com.hankcs.hanlp.corpus.occurrence.TermFrequency')
TermFrequencyCounter = JClass('com.hankcs.hanlp.mining.word.TermFrequencyCounter')

if __name__ == '__main__':
    counter = TermFrequencyCounter()
    counter.add("加油加油中国队！")  # 第一个文档
    counter.add("中国观众高呼加油中国")  # 第二个文档
    for termFrequency in counter:  # 遍历每个词与词频
        print("%s=%d" % (termFrequency.getTerm(), termFrequency.getFrequency()))
    print(counter.top(2))  # 取 top N

    #  根据词频提取关键词
    print(TermFrequencyCounter.getKeywordList("女排夺冠，观众欢呼女排女排女排！", 3))
