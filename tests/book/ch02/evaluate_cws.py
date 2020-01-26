# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-02 22:53
# 《自然语言处理入门》2.9 准确率评测
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
import re
from pyhanlp import *
from tests.test_utility import ensure_data


def to_region(segmentation: str) -> list:
    """
    将分词结果转换为区间
    :param segmentation: 商品 和 服务
    :return: [(0, 2), (2, 3), (3, 5)]
    """
    region = []
    start = 0
    for word in re.compile("\\s+").split(segmentation.strip()):
        end = start + len(word)
        region.append((start, end))
        start = end
    return region


def prf(gold: str, pred: str, dic) -> tuple:
    """
    计算P、R、F1
    :param gold: 标准答案文件，比如“商品 和 服务”
    :param pred: 分词结果文件，比如“商品 和服 务”
    :param dic: 词典
    :return: (P, R, F1, OOV_R, IV_R)
    """
    A_size, B_size, A_cap_B_size, OOV, IV, OOV_R, IV_R = 0, 0, 0, 0, 0, 0, 0
    with open(gold, encoding='utf-8') as gd, open(pred, encoding='utf-8') as pd:
        for g, p in zip(gd, pd):
            A, B = set(to_region(g)), set(to_region(p))
            A_size += len(A)
            B_size += len(B)
            A_cap_B_size += len(A & B)
            text = re.sub("\\s+", "", g)
            for (start, end) in A:
                word = text[start: end]
                if dic.containsKey(word):
                    IV += 1
                else:
                    OOV += 1

            for (start, end) in A & B:
                word = text[start: end]
                if dic.containsKey(word):
                    IV_R += 1
                else:
                    OOV_R += 1
    p, r = A_cap_B_size / B_size * 100, A_cap_B_size / A_size * 100
    return p, r, 2 * p * r / (p + r), OOV_R / OOV * 100, IV_R / IV * 100


if __name__ == '__main__':
    print(to_region('商品 和 服务'))

    sighan05 = ensure_data('icwb2-data', 'http://sighan.cs.uchicago.edu/bakeoff2005/data/icwb2-data.zip')
    msr_dict = os.path.join(sighan05, 'gold', 'msr_training_words.utf8')
    msr_test = os.path.join(sighan05, 'testing', 'msr_test.utf8')
    msr_output = os.path.join(sighan05, 'testing', 'msr_output.txt')
    msr_gold = os.path.join(sighan05, 'gold', 'msr_test_gold.utf8')

    DoubleArrayTrieSegment = JClass('com.hankcs.hanlp.seg.Other.DoubleArrayTrieSegment')
    segment = DoubleArrayTrieSegment([msr_dict]).enablePartOfSpeechTagging(True)
    with open(msr_gold, encoding='utf-8') as test, open(msr_output, 'w', encoding='utf-8') as output:
        for line in test:
            output.write("  ".join(term.word for term in segment.seg(re.sub("\\s+", "", line))))
            output.write("\n")
    print("P:%.2f R:%.2f F1:%.2f OOV-R:%.2f IV-R:%.2f" % prf(msr_gold, msr_output, segment.trie))
