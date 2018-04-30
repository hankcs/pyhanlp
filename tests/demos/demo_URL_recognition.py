# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_URL_recognition(text):
    """ 演示URL识别

    >>> text = '''HanLP的项目地址是https://github.com/hankcs/HanLP，
    ... 发布地址是https://github.com/hankcs/HanLP/releases，
    ... 我有时候会在www.hankcs.com上面发布一些消息，
    ... 我的微博是http://weibo.com/hankcs/，会同步推送hankcs.com的新闻。
    ... 听说.中国域名开放申请了,但我并没有申请hankcs.中国,因为穷……
    ... '''
    >>> demo_URL_recognition(text)
    [HanLP/nx, 的/ude1, 项目/n, 地址/n, 是/vshi, https://github.com/hankcs/HanLP/xu, ，/w,
    /w, 发布/v, 地址/n, 是/vshi, https://github.com/hankcs/HanLP/releases/xu, ，/w,
    /w, 我/rr, 有时候/d, 会/v, 在/p, www.hankcs.com/xu, 上面/f, 发布/v, 一些/m, 消息/n, ，/w,
    /w, 我/rr, 的/ude1, 微博/n, 是/vshi, http://weibo.com/hankcs//xu, ，/w, 会/v,
        同步/vd, 推送/nz, hankcs.com/xu, 的/ude1, 新闻/n, 。/w,
    /w, 听说/v, ./w, 中国/ns, 域名/n, 开放/v, 申请/v, 了/ule, ,/w, 但/c, 我/rr, 并/cc,
        没有/v, 申请/v, hankcs.中国/xu, ,/w, 因为/c, 穷/a, ……/w,
    /w]
    https://github.com/hankcs/HanLP
    https://github.com/hankcs/HanLP/releases
    www.hankcs.com
    http://weibo.com/hankcs/
    hankcs.com
    hankcs.中国
    """
    Nature = JClass("com.hankcs.hanlp.corpus.tag.Nature")
    Term = JClass("com.hankcs.hanlp.seg.common.Term")
    URLTokenizer = JClass("com.hankcs.hanlp.tokenizer.URLTokenizer")

    term_list = URLTokenizer.segment(text)
    print(term_list)
    for term in term_list:
        if term.nature == Nature.xu:
            print(term.word)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
