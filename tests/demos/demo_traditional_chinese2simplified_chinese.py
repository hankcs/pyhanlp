# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_traditional_chinese2simplified_chinese():
    """ 将简繁转换做到极致

    >>> demo_traditional_chinese2simplified_chinese()
    「以後等你當上皇后，就能買草莓慶祝了」。發現一根白頭髮
    凭借笔记本电脑写程序HanLP
    hankcs在臺灣寫程式碼
    hankcs在台湾写代码
    hankcs在香港寫代碼
    hankcs在香港写代码
    hankcs在臺灣寫程式碼
    hankcs在香港寫代碼
    hankcs在臺灣寫程式碼
    hankcs在台灣寫代碼
    hankcs在臺灣寫代碼
    hankcs在臺灣寫代碼
    """
    print(HanLP.convertToTraditionalChinese("“以后等你当上皇后，就能买草莓庆祝了”。发现一根白头发"))
    print(HanLP.convertToSimplifiedChinese("憑藉筆記簿型電腦寫程式HanLP"))
    # 简体转台湾繁体
    print(HanLP.s2tw("hankcs在台湾写代码"))
    # 台湾繁体转简体
    print(HanLP.tw2s("hankcs在臺灣寫程式碼"))
    # 简体转香港繁体
    print(HanLP.s2hk("hankcs在香港写代码"))
    # 香港繁体转简体
    print(HanLP.hk2s("hankcs在香港寫代碼"))
    # 香港繁体转台湾繁体
    print(HanLP.hk2tw("hankcs在臺灣寫代碼"))
    # 台湾繁体转香港繁体
    print(HanLP.tw2hk("hankcs在香港寫程式碼"))

    # 香港/台湾繁体和HanLP标准繁体的互转
    print(HanLP.t2tw("hankcs在臺灣寫代碼"))
    print(HanLP.t2hk("hankcs在臺灣寫代碼"))

    print(HanLP.tw2t("hankcs在臺灣寫程式碼"))
    print(HanLP.hk2t("hankcs在台灣寫代碼"))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
