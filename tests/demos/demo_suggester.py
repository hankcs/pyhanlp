# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_suggester():
    """ 文本推荐(句子级别，从一系列句子中挑出与输入句子最相似的那一个)

    >>> demo_suggester()
    [威廉王子发表演说 呼吁保护野生动物, 英报告说空气污染带来“公共健康危机”]
    [英报告说空气污染带来“公共健康危机”]
    [《时代》年度人物最终入围名单出炉 普京马云入选]
    [魅惑天后许佳慧不爱“预谋” 独唱《许某某》]
    """
    Suggester = JClass("com.hankcs.hanlp.suggest.Suggester")
    suggester = Suggester()
    title_array = [
        "威廉王子发表演说 呼吁保护野生动物",
        "魅惑天后许佳慧不爱“预谋” 独唱《许某某》",
        "《时代》年度人物最终入围名单出炉 普京马云入选",
        "“黑格比”横扫菲：菲吸取“海燕”经验及早疏散",
        "日本保密法将正式生效 日媒指其损害国民知情权",
        "英报告说空气污染带来“公共健康危机”"
    ]
    for title in title_array:
        suggester.addSentence(title)

    print(suggester.suggest("陈述", 2))      # 语义
    print(suggester.suggest("危机公关", 1))  # 字符
    print(suggester.suggest("mayun", 1))   # 拼音
    print(suggester.suggest("徐家汇", 1)) # 拼音


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
