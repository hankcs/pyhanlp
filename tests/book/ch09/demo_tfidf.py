# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-08-01 18:25
# 《自然语言处理入门》9.2 关键词提取
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *

TfIdfCounter = JClass('com.hankcs.hanlp.mining.word.TfIdfCounter')

if __name__ == '__main__':
    counter = TfIdfCounter()
    counter.add("《女排夺冠》", "女排北京奥运会夺冠")  # 输入多篇文档
    counter.add("《羽毛球男单》", "北京奥运会的羽毛球男单决赛")
    counter.add("《女排》", "中国队女排夺北京奥运会金牌重返巅峰，观众欢呼女排女排女排！")
    counter.compute()  # 输入完毕
    for id in counter.documents():
        print(id + " : " + counter.getKeywordsOf(id, 3).toString())  # 根据每篇文档的TF-IDF提取关键词
    # 根据语料库已有的IDF信息为语料库之外的新文档提取关键词
    print(counter.getKeywords("奥运会反兴奋剂", 2))
