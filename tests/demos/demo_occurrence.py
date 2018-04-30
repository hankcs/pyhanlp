# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_occurrence():
    """ 演示词共现统计

    >>> demo_occurrence()
    信息=1
    先进=1
    图形图像=1
    处理=2
    技术=1
    方面=1
    比较=1
    目前=1
    算法=2
    视频=1
    计算机=1
    音视频=1
    <BLANKLINE>
    信息→算法= tf=1 mi=8.856243954648566 le=0.0 re=0.0 score=NaN
    先进→视频= tf=1 mi=6.594180024229758 le=0.0 re=0.0 score=NaN
    图形图像→技术= tf=1 mi=20.46090157247892 le=0.0 re=0.0 score=NaN
    处理→方面= tf=1 mi=4.04319404601706 le=0.0 re=0.0 score=NaN
    处理→算法= tf=1 mi=9.247593120777918 le=0.0 re=0.0 score=NaN
    技术→信息= tf=1 mi=4.012478779454232 le=0.0 re=0.0 score=NaN
    方面→目前= tf=1 mi=12.825210015738996 le=0.0 re=0.0 score=NaN
    比较→先进= tf=1 mi=6.050081533887511 le=0.0 re=0.0 score=NaN
    目前→比较= tf=1 mi=13.377862072309142 le=0.0 re=0.0 score=NaN
    算法→处理= tf=1 mi=9.247593120777918 le=0.0 re=0.0 score=NaN
    视频→处理= tf=1 mi=5.139944592929454 le=0.0 re=0.0 score=NaN
    计算机→音视频= tf=1 mi=20.46090157247892 le=0.0 re=0.0 score=NaN
    音视频→图形图像= tf=1 mi=20.46090157247892 le=0.0 re=0.0 score=NaN
    <BLANKLINE>
    信息→算法→处理= tf=1 mi=0.0 le=0.0 re=0.0
    先进→视频→处理= tf=1 mi=0.0 le=0.0 re=0.0
    图形图像→技术→信息= tf=1 mi=0.0 le=0.0 re=0.0
    处理→方面→目前= tf=1 mi=0.0 le=0.0 re=0.0
    技术→信息→算法= tf=1 mi=0.0 le=0.0 re=0.0
    方面→目前→比较= tf=1 mi=0.0 le=0.0 re=0.0
    比较→先进→视频= tf=1 mi=0.0 le=0.0 re=0.0
    目前→比较→先进= tf=1 mi=0.0 le=0.0 re=0.0
    算法→处理→方面= tf=1 mi=0.0 le=0.0 re=0.0
    视频→处理→算法= tf=1 mi=0.0 le=0.0 re=0.0
    计算机→音视频→图形图像= tf=1 mi=0.0 le=0.0 re=0.0
    音视频→图形图像→技术= tf=1 mi=0.0 le=0.0 re=0.0

    """
    Occurrence = JClass("com.hankcs.hanlp.corpus.occurrence.Occurrence")
    PairFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.PairFrequency")
    TermFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.TermFrequency")
    TriaFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.TriaFrequency")

    occurrence = Occurrence()
    occurrence.addAll("在计算机音视频和图形图像技术等二维信息算法处理方面目前比较先进的视频处理算法")
    occurrence.compute()

    unigram = occurrence.getUniGram()
    for entry in unigram.iterator():
        term_frequency = entry.getValue()
        print(term_frequency)
    print()

    bigram = occurrence.getBiGram()
    for entry in bigram.iterator():
        pair_frequency = entry.getValue()
        if pair_frequency.isRight():
            print(pair_frequency)
    print()

    trigram = occurrence.getTriGram()
    for entry in trigram.iterator():
        tria_frequency = entry.getValue()
        if tria_frequency.isRight():
            print(tria_frequency)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
