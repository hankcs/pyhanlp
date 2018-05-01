# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_NLP_segment():
    """ NLP分词，更精准的中文分词、词性标注与命名实体识别
        标注集请查阅 https://github.com/hankcs/HanLP/blob/master/data/dictionary/other/TagPKU98.csv
        或者干脆调用 Sentence#translateLabels() 转为中文

    >>> demo_NLP_segment()
    [我/r, 新造/v, 一个/m, 词/n, 叫/v, 幻想乡/ns, 你/r, 能/v, 识别/v, 并/c, 正确/ad, 标注/v, 词性/n, 吗/y, ？/w]
    我/代词 的/助词 希望/名词 是/动词 希望/动词 张晚霞/人名 的/助词 背影/名词 被/介词 晚霞/名词 映/动词 红/形容词
    支援/v 臺灣/ns 正體/n 香港/ns 繁體/n ：/w [微软/nt 公司/n]/nt 於/p 1975年/t 由/p 比爾·蓋茲/n 和/c 保羅·艾倫/nr 創立/v 。/w
    """
    NLPTokenizer = JClass("com.hankcs.hanlp.tokenizer.NLPTokenizer")
    print(NLPTokenizer.segment("我新造一个词叫幻想乡你能识别并正确标注词性吗？"))  # “正确”是副形词。
    # 注意观察下面两个“希望”的词性、两个“晚霞”的词性
    print(NLPTokenizer.analyze("我的希望是希望张晚霞的背影被晚霞映红").translateLabels())
    print(NLPTokenizer.analyze("支援臺灣正體香港繁體：微软公司於1975年由比爾·蓋茲和保羅·艾倫創立。"))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
