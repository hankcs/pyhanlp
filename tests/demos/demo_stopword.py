# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_stopword():
    """ 演示文本分类最基本的调用方式
        中文情感挖掘语料-ChnSentiCorp 谭松波

    TO-DO: 还可以自定义过滤逻辑

    >>> demo_stopword()
    [小区/n, 反对/v, 喂养/v, 流浪猫/nz, 赞成/v, 喂养/v, 小宝贝/nz]
    [小区/n, 居民/n, 反对/v, 喂养/v, 流浪猫/nz, 居民/n, 赞成/v, 喂养/v, 小宝贝/nz]
    [小区/n, 居民/n, 有/vyou, 的/ude1, 反对/v, 喂养/v, 流浪猫/nz, ，/w, 而/cc, 有的/rz, 居民/n, 却/d, 赞成/v, 喂养/v, 这些/rz, 小宝贝/nz]
    [小区/n, 居民/n, 反对/v, 喂养/v, 流浪猫/nz, 居民/n, 赞成/v, 喂养/v, 小宝贝/nz]
    """
    CoreStopWordDictionary = JClass("com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary")
    Filter = JClass("com.hankcs.hanlp.dictionary.stopword.Filter")
    Term = JClass("com.hankcs.hanlp.seg.common.Term")
    BasicTokenizer = JClass("com.hankcs.hanlp.tokenizer.BasicTokenizer")
    NotionalTokenizer =JClass("com.hankcs.hanlp.tokenizer.NotionalTokenizer")

    text = "小区居民有的反对喂养流浪猫，而有的居民却赞成喂养这些小宝贝"
    # 可以动态修改停用词词典
    CoreStopWordDictionary.add("居民")
    print(NotionalTokenizer.segment(text))
    CoreStopWordDictionary.remove("居民")
    print(NotionalTokenizer.segment(text))

    # 可以对任意分词器的结果执行过滤
    term_list = BasicTokenizer.segment(text)
    print(term_list)
    CoreStopWordDictionary.apply(term_list)
    print(term_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
