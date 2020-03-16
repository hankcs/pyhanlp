# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-04 17:41
# 《自然语言处理入门》8.5.3 基于感知机序列标注的命名实体识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
import os

from tests.test_utility import ensure_data

MSRA_NER = ensure_data("msra-ne", "http://file.hankcs.com/corpus/msra-ne.zip")
MSRA_NER_TRAIN = os.path.join(MSRA_NER, 'train.txt')
MSRA_NER_TEST = os.path.join(MSRA_NER, 'test.txt')
MSRA_NER_MODEL = os.path.join(MSRA_NER, 'model.bin')