# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-29
from pyhanlp import *


def demo_custom_dictionary(text):
    """ 演示用户词典的动态增删
    TO-DO:
    DoubleArrayTrie分词
    首字哈希之后二分的trie树分词

    >>> text = "攻城狮逆袭单身狗，迎娶白富美，走上人生巅峰"  # 怎么可能噗哈哈！
    >>> demo_custom_dictionary(text)
    [攻城/vi, 狮/ng, 逆袭/nz, 单身/n, 狗/n, ，/w, 迎娶/v, 白富美/nr, ，/w, 走上/v, 人生/n, 巅峰/n]
    [攻城狮/nz, 逆袭/nz, 单身狗/nz, ，/w, 迎娶/v, 白富美/nz, ，/w, 走上/v, 人生/n, 巅峰/n]
    """
    print(HanLP.segment(text))

    CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    CustomDictionary.add("攻城狮")  # 动态增加
    CustomDictionary.insert("白富美", "nz 1024")  # 强行插入
    #CustomDictionary.remove("攻城狮"); # 删除词语（注释掉试试）
    CustomDictionary.add("单身狗", "nz 1024 n 1")
    #print(CustomDictionary.get("单身狗"))

    print(HanLP.segment(text))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
