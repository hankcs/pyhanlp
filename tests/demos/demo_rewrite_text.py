# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_rewrite_text():
    """ 同义改写

    >>> demo_rewrite_text()
    此点子可以使同义词词典将一律段文本改写成意思相似之另一样段落文本，而且多符合语法
    """
    CoreSynonymDictionary = JClass("com.hankcs.hanlp.dictionary.CoreSynonymDictionary")
    text = "这个方法可以利用同义词词典将一段文本改写成意思相似的另一段文本，而且差不多符合语法"
    print(CoreSynonymDictionary.rewrite(text))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
