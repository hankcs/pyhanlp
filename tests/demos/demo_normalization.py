# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_normalization():
    """ 演示正规化字符配置项的效果（繁体->简体，全角->半角，大写->小写）。
        该配置项位于hanlp.properties中，通过Normalization=true来开启
        切换配置后必须删除CustomDictionary.txt.bin缓存，否则只影响动态插入的新词。

    >>> demo_normalization()
    [爱听4g/nz]
    [爱听4g/nz]
    [爱听4g/nz]
    [爱听4g/nz]
    [爱听4g/nz]
    """
    CustomDictionary =JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    Config = JClass("com.hankcs.hanlp.HanLP$Config")

    Config.Normalization = True
    CustomDictionary.insert("爱听4G", "nz 1000")
    print(HanLP.segment("爱听4g"))
    print(HanLP.segment("爱听4G"))
    print(HanLP.segment("爱听４G"))
    print(HanLP.segment("爱听４Ｇ"))
    print(HanLP.segment("愛聽４Ｇ"))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
