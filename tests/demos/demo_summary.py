# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_summary(document):
    """自动摘要

    >>> document = '''水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，
    ... 根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，
    ... 有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，
    ... 严格地进行水资源论证和取水许可的批准。
    ... '''
    >>> demo_summary(document)
    [严格地进行水资源论证和取水许可的批准,
    水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露,
    有部分省超过红线的指标]
    """

    TextRankSentence = JClass("com.hankcs.hanlp.summary.TextRankSentence")
    sentence_list = HanLP.extractSummary(document, 3)
    print(sentence_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
