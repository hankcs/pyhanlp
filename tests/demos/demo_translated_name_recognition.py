# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_translated_name_recognition(sentences):
    """ 音译人名识别

    >>> sentences = [
    ... "一桶冰水当头倒下，微软的比尔盖茨、Facebook的扎克伯格跟桑德博格、亚马逊的贝索斯、苹果的库克全都不惜湿身入镜，这些硅谷的科技人，飞蛾扑火似地牺牲演出，其实全为了慈善。",
    ... "世界上最长的姓名是简森·乔伊·亚历山大·比基·卡利斯勒·达夫·埃利奥特·福克斯·伊维鲁莫·马尔尼·梅尔斯·帕特森·汤普森·华莱士·普雷斯顿。",
    ... ]
    >>> demo_translated_name_recognition(sentences)
    [一桶/nz, 冰水/n, 当头/vi, 倒下/v, ，/w, 微软/ntc, 的/ude1, 比尔盖茨/nrf, 、/w,
        Facebook/nx, 的/ude1, 扎克伯格/nrf, 跟/p, 桑德博格/nrf, 、/w, 亚马逊/nrf, 的/ude1,
        贝索斯/nrf, 、/w, 苹果/nf, 的/ude1, 库克/nrf, 全都/d, 不惜/v, 湿身/nz, 入镜/nz, ，/w,
        这些/rz, 硅谷/ns, 的/ude1, 科技/n, 人/n, ，/w, 飞蛾扑火/nz, 似地/d, 牺牲/v,
        演出/vn, ，/w, 其实/d, 全/a, 为了/p, 慈善/a, 。/w]
    [世界/n, 上/f, 最长/d, 的/ude1, 姓名/n, 是/vshi,
        简森·乔伊·亚历山大·比基·卡利斯勒·达夫·埃利奥特·福克斯·伊维鲁莫·马尔尼·梅尔斯·帕特森·汤普森·华莱士·普雷斯顿/nrf, 。/w]
    """
    segment = HanLP.newSegment().enableTranslatedNameRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
