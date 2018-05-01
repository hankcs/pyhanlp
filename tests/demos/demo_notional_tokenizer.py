# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_notional_tokenizer():
    """ 演示自动去除停用词、自动断句的分词器

    >>> demo_notional_tokenizer()
    [小区/n, 居民/n, 反对/v, 喂养/v, 流浪猫/nz, 居民/n, 赞成/v, 喂养/v, 小宝贝/nz]
    [小区/n, 居民/n, 反对/v, 喂养/v, 流浪猫/nz]
    [居民/n, 赞成/v, 喂养/v, 小宝贝/nz]
    """
    Term =JClass("com.hankcs.hanlp.seg.common.Term")
    NotionalTokenizer = JClass("com.hankcs.hanlp.tokenizer.NotionalTokenizer")

    text = "小区居民有的反对喂养流浪猫，而有的居民却赞成喂养这些小宝贝"
    print(NotionalTokenizer.segment(text))
    for sentence in NotionalTokenizer.seg2sentence(text):
        print(sentence)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
