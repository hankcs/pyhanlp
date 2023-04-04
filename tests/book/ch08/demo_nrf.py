# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2023-04-04 13:47
# 《自然语言处理入门》8.2 基于规则的命名实体识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *

DijkstraSegment = JClass('com.hankcs.hanlp.seg.Dijkstra.DijkstraSegment')
CoreBiGramTableDictionary = JClass('com.hankcs.hanlp.dictionary.CoreBiGramTableDictionary')


HanLP.Config.enableDebug()
sent = "我知道卡利斯勒出生于英格兰"
segment = DijkstraSegment().enableTranslatedNameRecognize(True)
print(segment.seg(sent))

if CoreBiGramTableDictionary.getBiFrequency("未##人", "出生于") == 0:
    with open(HanLP.Config.BiGramDictionaryPath, 'a') as out:
        out.write('\n未##人@出生于 1\n')
    CoreBiGramTableDictionary.reload()
    print(segment.seg(sent))
