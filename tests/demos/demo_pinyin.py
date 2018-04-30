# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_pinyin():
    """ 汉字转拼音

    >>> demo_pinyin()
    原文， 重载不是重任！
    拼音（数字音调）， [chong2, zai3, bu2, shi4, zhong4, ren4, none5]
    拼音（符号音调）， chóng, zǎi, bú, shì, zhòng, rèn, none,
    拼音（无音调）， chong, zai, bu, shi, zhong, ren, none,
    声调， 2, 3, 2, 4, 4, 4, 5,
    声母， ch, z, b, sh, zh, r, none,
    韵母， ong, ai, u, i, ong, en, none,
    输入法头， ch, z, b, sh, zh, r, none,
    jie zhi none none none none nian none
    jie zhi 2 0 1 2 nian ，
    """
    Pinyin = JClass("com.hankcs.hanlp.dictionary.py.Pinyin")
    text = "重载不是重任！"
    pinyin_list = HanLP.convertToPinyinList(text)

    print("原文，", end=" ")
    print(text)
    print("拼音（数字音调），", end=" ")
    print(pinyin_list)
    print("拼音（符号音调），", end=" ")
    for pinyin in pinyin_list:
        print("%s," % pinyin.getPinyinWithToneMark(), end=" ")
    print("\n拼音（无音调），", end=" ")
    for pinyin in pinyin_list:
        print("%s," % pinyin.getPinyinWithoutTone(), end=" ")
    print("\n声调，", end=" ")
    for pinyin in pinyin_list:
        print("%s," % pinyin.getTone(), end=" ")
    print("\n声母，", end=" ")
    for pinyin in pinyin_list:
        print("%s," % pinyin.getShengmu(), end=" ")
    print("\n韵母，", end=" ")
    for pinyin in pinyin_list:
        print("%s," % pinyin.getYunmu(), end=" ")
    print("\n输入法头，", end=" ")
    for pinyin in pinyin_list:
        print("%s," % pinyin.getHead(), end=" ")

    print()
    # 拼音转换可选保留无拼音的原字符
    print(HanLP.convertToPinyinString("截至2012年，", " ", True))
    print(HanLP.convertToPinyinString("截至2012年，", " ", False))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
