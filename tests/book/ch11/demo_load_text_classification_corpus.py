# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-01-03 19:36
# 《自然语言处理入门》11.2 文本分类语料库
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.demos.demo_text_classification import sogou_corpus_path

AbstractDataSet = JClass('com.hankcs.hanlp.classification.corpus.AbstractDataSet')
Document = JClass('com.hankcs.hanlp.classification.corpus.Document')
FileDataSet = JClass('com.hankcs.hanlp.classification.corpus.FileDataSet')
MemoryDataSet = JClass('com.hankcs.hanlp.classification.corpus.MemoryDataSet')

# 演示加载文本分类语料库
if __name__ == '__main__':
    dataSet = MemoryDataSet()  # ①将数据集加载到内存中
    dataSet.load(sogou_corpus_path)  # ②加载data/test/搜狗文本分类语料库迷你版
    dataSet.add("自然语言处理", "自然语言处理很有趣")  # ③新增样本
    allClasses = dataSet.getCatalog().getCategories()  # ④获取标注集
    print("标注集：%s" % (allClasses))
    for document in dataSet.iterator():
        print("第一篇文档的类别：" + allClasses.get(document.category))
        break
