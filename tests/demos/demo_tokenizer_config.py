# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_tokenizer_config(text):
    """ 演示动态设置预置分词器，这里的设置是全局的

    >>> text = "泽田依子是上外日本文化经济学院的外教"
    >>> demo_tokenizer_config(text)
    [泽田依/nr, 子/ng, 是/vshi, 上外/nit, 日本/ns, 文化/n, 经济学院/nit, 的/ude1, 外教/n]
    [泽田依子/nrj, 是/vshi, 上外日本文化经济学院/nt, 的/ude1, 外教/n]
    """
    StandardTokenizer = JClass("com.hankcs.hanlp.tokenizer.StandardTokenizer")
    print(StandardTokenizer.segment(text))
    StandardTokenizer.SEGMENT.enableAllNamedEntityRecognize(True)
    print(StandardTokenizer.segment(text))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
