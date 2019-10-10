# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-05 16:14
# 《自然语言处理入门》7.4 自定义词性
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from pyhanlp import *

CustomDictionary.insert("苹果", "手机品牌 1")
CustomDictionary.insert("iPhone X", "手机型号 1")
analyzer = PerceptronLexicalAnalyzer()
analyzer.enableCustomDictionaryForcing(True)
print(analyzer.analyze("你们苹果iPhone X保修吗？"))
print(analyzer.analyze("多吃苹果有益健康"))
