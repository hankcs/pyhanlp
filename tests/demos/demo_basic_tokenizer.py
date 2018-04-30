# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-29
from pyhanlp import *
import time


def demo_basic_tokenizer(text):
    """ 演示基础分词，基础分词只进行基本NGram分词，不识别命名实体，不使用用户词典

    >>> text = ("举办纪念活动铭记二战历史，不忘战争带给人类的深重灾难，是为了防止悲剧重演，确保和平永驻；"
    ...    "铭记二战历史，更是为了提醒国际社会，需要共同捍卫二战胜利成果和国际公平正义，"
    ...    "必须警惕和抵制在历史认知和维护战后国际秩序问题上的倒行逆施。")
    >>> demo_basic_tokenizer(text)
    [举办/v, 纪念活动/nz, 铭记/v, 二战/n, 历史/n, ，/w, 不忘/v, 战争/n, 带给/v, 人类/n,
     的/ude1, 深重/a, 灾难/n, ，/w, 是/vshi, 为了/p, 防止/v, 悲剧/n, 重演/v, ，/w, 确保/v,
     和平/n, 永驻/nz, ；/w, 铭记/v, 二战/n, 历史/n, ，/w, 更是/d, 为了/p, 提醒/v, 国际/n,
      社会/n, ，/w, 需要/v, 共同/d, 捍卫/v, 二战/n, 胜利/vn, 成果/n, 和/cc, 国际/n, 公平/a,
       正义/n, ，/w, 必须/d, 警惕/v, 和/cc, 抵制/v, 在/p, 历史/n, 认知/vn, 和/cc, 维护/v,
       战后/t, 国际/n, 秩序/n, 问题/n, 上/f, 的/ude1, 倒行逆施/vl, 。/w]
    BasicTokenizer分词速度：1499051.04字每秒
    """
    BasicTokenizer = JClass("com.hankcs.hanlp.tokenizer.BasicTokenizer")
    print(BasicTokenizer.segment(text))

    start = time.time()
    pressure = 100000
    for i in range(pressure):
        BasicTokenizer.segment(text)
    cost_time = time.time() - start
    print("BasicTokenizer分词速度：%.2f字每秒" % (
        len(text) * pressure / cost_time))

if __name__ == "__main__":
    import doctest
    # doctest.NORMALIZE_WHITESPACE 输出比对的文档，忽略换行等空格。防止一行过长
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
