# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-02 14:43
# 《自然语言处理入门》6.4 HanLP 中的 CRF++ API
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from pyhanlp import *
from tests.book.ch03 import msr
from tests.book.ch03.eval_bigram_cws import CWSEvaluator
from tests.book.ch06.crfpp_train_hanlp_load import CRF_MODEL_PATH, CRF_MODEL_TXT_PATH

CRFSegmenter = JClass('com.hankcs.hanlp.model.crf.CRFSegmenter')
CRFLexicalAnalyzer = JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')


def train(corpus):
    segmenter = CRFSegmenter(None)
    segmenter.train(corpus, CRF_MODEL_PATH)
    return CRFLexicalAnalyzer(segmenter)
    # 训练完毕时，可传入txt格式的模型（不可传入CRF++的二进制模型，不兼容！）
    # return CRFLexicalAnalyzer(CRF_MODEL_TXT_PATH).enableCustomDictionary(False)


if __name__ == '__main__':
    segment = train(msr.msr_train)
    print(CWSEvaluator.evaluate(segment, msr.msr_test, msr.msr_output, msr.msr_gold, msr.msr_dict))  # 标准化评测
