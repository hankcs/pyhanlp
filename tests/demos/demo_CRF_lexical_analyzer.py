# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_CRF_lexical_analyzer(tests):
    """ CRF词法分析器

    >>> tests = ["商品和服务",
    ... "上海华安工业（集团）公司董事长谭旭光和秘书胡花蕊来到美国纽约现代艺术博物馆参观",
    ... "微软公司於1975年由比爾·蓋茲和保羅·艾倫創立，18年啟動以智慧雲端、前端為導向的大改組。"]
    >>> demo_CRF_lexical_analyzer(tests)
    商品/n 和/c 服务/vn
    [上海/ns 华安/nz 工业/n （/n 集团/n ）/v 公司/n]/nt 董事长/n 谭旭光/nr 和/c 秘书/n
        胡花蕊/nr 来到/v [美国/ns 纽约/ns 现代/t 艺术/n 博物馆/n]/ns 参观/v
    [微软/nt 公司/n]/nt 於/p 1975年/t 由/p 比爾·蓋茲/n 和/c 保羅·艾倫/v 創立/v ，/v
        18年/n 啟動/v 以/p 智慧/n 雲端/n 、/v 前端/n 為/v 導向/n 的/u 大/a 改組/vn 。/w
    """
    CRFLexicalAnalyzer = JClass("com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer")
    analyzer = CRFLexicalAnalyzer()
    for sentence in tests:
        print(analyzer.analyze(sentence))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
