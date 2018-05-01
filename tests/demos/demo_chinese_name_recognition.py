# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-29
from pyhanlp import *

def demo_chinese_name_recognition(sentences):
    """ 中国人名识别

    >>> sentences = [
    ...    "签约仪式前，秦光荣、李纪恒、仇和等一同会见了参加签约的企业家。",
    ...    "武大靖创世界纪录夺冠，中国代表团平昌首金",
    ...    "区长庄木弟新年致辞",
    ...    "朱立伦：两岸都希望共创双赢 习朱历史会晤在即",
    ...    "陕西首富吴一坚被带走 与令计划妻子有交集",
    ...    "据美国之音电台网站4月28日报道，8岁的凯瑟琳·克罗尔（凤甫娟）和很多华裔美国小朋友一样，小小年纪就开始学小提琴了。她的妈妈是位虎妈么？",
    ...    "凯瑟琳和露西（庐瑞媛），跟她们的哥哥们有一些不同。",
    ...    "王国强、高峰、汪洋、张朝阳光着头、韩寒、小四",
    ...    "张浩和胡健康复员回家了",
    ...    "王总和小丽结婚了",
    ...    "编剧邵钧林和稽道青说",
    ...    "这里有关天培的有关事迹",
    ...    "龚学平等领导说,邓颖超生前杜绝超生",]
    >>> demo_chinese_name_recognition(sentences)
    [签约/vi, 仪式/n, 前/f, ，/w, 秦光荣/nr, 、/w, 李纪恒/nr, 、/w, 仇和/nr, 等/udeng, 一同/d, 会见/v, 了/ule, 参加/v, 签约/vi, 的/ude1, 企业家/nnt, 。/w]
    [武大靖/nr, 创/v, 世界纪录/nz, 夺冠/vi, ，/w, 中国代表团/nt, 平昌/ns, 首金/n]
    [区长/nnt, 庄木弟/nr, 新年/t, 致辞/vi]
    [朱立伦/nr, ：/w, 两岸/n, 都/d, 希望/v, 共创/v, 双赢/n,  /w, 习/v, 朱/ag, 历史/n, 会晤/vn, 在即/vi]
    [陕西/ns, 首富/n, 吴一坚/nr, 被/pbei, 带走/v,  /w, 与/cc, 令计划/nr, 妻子/n, 有/vyou, 交集/v]
    [据/p, 美国之音/n, 电台/nis, 网站/n, 4/m, 月/n, 28/m, 日/b, 报道/v, ，/w, 8/m, 岁/qt, 的/ude1, 凯瑟琳·克罗尔/nrf, （/w, 凤甫娟/nr, ）/w, 和/cc, 很多/m, 华裔/n, 美国/nsf, 小朋友/n, 一样/uyy, ，/w, 小小年纪/n, 就/d, 开始/v, 学/v, 小提琴/n, 了/ule, 。/w, 她/rr, 的/ude1, 妈妈/n, 是/vshi, 位/q, 虎妈/nz, 么/y, ？/w]
    [凯瑟琳/nrf, 和/cc, 露西/nrf, （/w, 庐瑞媛/nr, ）/w, ，/w, 跟/p, 她们/rr, 的/ude1, 哥哥/n, 们/k, 有/vyou, 一些/m, 不同/a, 。/w]
    [王国强/nr, 、/w, 高峰/n, 、/w, 汪洋/n, 、/w, 张朝阳/nr, 光着头/l, 、/w, 韩寒/nr, 、/w, 小/a, 四/m]
    [张浩/nr, 和/cc, 胡健康/nr, 复员/v, 回家/vi, 了/ule]
    [王总/nr, 和/cc, 小丽/nr, 结婚/vi, 了/ule]
    [编剧/nnt, 邵钧林/nr, 和/cc, 稽道青/nr, 说/v]
    [这里/rzs, 有/vyou, 关天培/nr, 的/ude1, 有关/vn, 事迹/n]
    [龚学平/nr, 等/udeng, 领导/n, 说/v, ,/w, 邓颖超/nr, 生前/t, 杜绝/v, 超生/vi]
    """
    segment = HanLP.newSegment().enableNameRecognize(True);
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
