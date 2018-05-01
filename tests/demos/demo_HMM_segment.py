# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-29
from pyhanlp import *
import time


def demo_HMM_segment():
    """ 演示二阶隐马分词，这是一种基于字标注的分词方法，对未登录词支持较好，对已登录词的分词速度慢。综合性能不如CRF分词。
        还未稳定，请不要用于生产环境。二阶隐马标注分词效果尚且不好，许多开源分词器使用甚至使用一阶隐马（BiGram二元文法），
        效果可想而知。对基于字符的序列标注分词方法，hackcs只推荐CRF。

    >>> demo_HMM_segment()
    [HanLP是, 由, 一系列, 模型, 与, 算法, 组成, 的, Java, 工具, 包, ，, 目标, 是, 普及, 自然语言处理, 在, 生产, 环境, 中的, 应用, 。]
    [高锰酸钾, ，, 强氧化剂, ，, 紫红色, 晶体, ，, 可, 溶于, 水, ，, 遇乙醇, 即, 被, 还原,
        。, 常, 用作, 消毒, 剂, 、, 水, 净化剂, 、, 氧化剂, 、, 漂白剂, 、, 毒气, 吸收剂, 、, 二氧化碳, 精制剂, 等, 。]
    [《, 夜晚, 的, 骰子, 》, 通过, 描述, 浅草, 的, 舞女, 在, 暗夜, 中, 扔骰子, 的, 情景, ,, 寄托, 了, 作者, 对, 庶民, 生活区, 的, 情感]
    [这个, 像是, 真的, [, 委屈, ], 前面, 那个, 打扮, 太, 江, 户, 了, ，, 一点, 不, 上品, ..., @, hankcs]
    [鼎泰丰, 的, 小笼, 一点, 味道, 也, 没有, ..., 每样, 都, 淡淡, 的, ..., 淡淡的, ，, 哪, 有, 食堂, 2A, 的, 好次]
    [克里斯蒂娜·克罗尔, 说, ：, 不, ，, 我, 不是, 虎妈, 。, 我, 全家, 都, 热爱, 音乐, ，, 我, 也, 鼓励, 他们, 这么, 做, 。]
    [今日, APPS, ：, Sago , Mini , Toolbox, 培养, 孩子, 动手, 能力]
    [财政部, 副部长, 王保安, 调任, 国家统计局, 党组书记]
    [2, ., 34, 米, 男子, 娶, 1, ., 53, 米, 女, 粉丝,  , 称, 夫妻生活, 没问题]
    [你, 看过, 穆赫, 兰道, 吗]
    [乐, 视, 超级, 手机, 能否, 承载, 贾布斯, 的, 生态, 梦]
    [江西, 鄱阳湖, 干枯, ，, 中国, 最大, 淡水湖, 变成, 大草原]
    HMM2分词速度：53705.79字每秒
    """
    HMMSegment = JClass("com.hankcs.hanlp.seg.HMM.HMMSegment")
    Segment = JClass("com.hankcs.hanlp.seg.Segment")
    Term = JClass("com.hankcs.hanlp.seg.common.Term")

    JClass("com.hankcs.hanlp.HanLP$Config").ShowTermNature = False
    segment = HMMSegment()
    sentence_array = [
        "HanLP是由一系列模型与算法组成的Java工具包，目标是普及自然语言处理在生产环境中的应用。",
        "高锰酸钾，强氧化剂，紫红色晶体，可溶于水，遇乙醇即被还原。常用作消毒剂、水净化剂、氧化剂、漂白剂、毒气吸收剂、二氧化碳精制剂等。", # 专业名词有一定辨识能力
        "《夜晚的骰子》通过描述浅草的舞女在暗夜中扔骰子的情景,寄托了作者对庶民生活区的情感",    # 非新闻语料
        "这个像是真的[委屈]前面那个打扮太江户了，一点不上品...@hankcs",  # 微博
        "鼎泰丰的小笼一点味道也没有...每样都淡淡的...淡淡的，哪有食堂2A的好次",
        "克里斯蒂娜·克罗尔说：不，我不是虎妈。我全家都热爱音乐，我也鼓励他们这么做。",
        "今日APPS：Sago Mini Toolbox培养孩子动手能力",
        "财政部副部长王保安调任国家统计局党组书记",
        "2.34米男子娶1.53米女粉丝 称夫妻生活没问题",
        "你看过穆赫兰道吗",
        "乐视超级手机能否承载贾布斯的生态梦"]

    for sentence in sentence_array:
        term_list = segment.seg(sentence)
        print(term_list)


    # 测个速度
    text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原"
    print(segment.seg(text))
    start = time.time()
    pressure = 1000
    for i in range(pressure):
        segment.seg(text)
    cost_time = time.time() - start
    print("HMM2分词速度：%.2f字每秒" % (len(text) * pressure / cost_time))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
