# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-08 15:34
# 《自然语言处理入门》3.5.3 调整模型
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import HanLP
from tests.book.ch03.msr import msr_model
from tests.book.ch03.ngram_segment import load_bigram, CoreDictionary

segment = load_bigram(model_path=msr_model, verbose=False, ret_viterbi=False)
assert CoreDictionary.contains("管道")
text = "北京输气管道工程"
HanLP.Config.enableDebug()
print(segment.seg(text))