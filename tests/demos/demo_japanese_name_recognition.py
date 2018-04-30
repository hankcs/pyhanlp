# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-29
from pyhanlp import *


def demo_japanese_name_recognition(sentences):
    """ 日本人名识别

    >>> sentences =[
    ...    "北川景子参演了林诣彬导演的《速度与激情3》",
    ...    "林志玲亮相网友:确定不是波多野结衣？",
    ...    "龟山千广和近藤公园在龟山公园里喝酒赏花",
    ... ]
    >>> demo_japanese_name_recognition(sentences)
    [北川景子/nrj, 参演/v, 了/ule, 林诣彬/nr, 导演/nnt, 的/ude1, 《/w, 速度/n, 与/cc, 激情/n, 3/m, 》/w]
    [林志玲/nr, 亮相/vi, 网友/n, :/w, 确定/v, 不是/c, 波多野结衣/nrj, ？/w]
    [龟山千广/nrj, 和/cc, 近藤公园/nrj, 在/p, 龟山/nz, 公园/n, 里/f, 喝酒/vi, 赏花/nz]
    """
    Segment = JClass("com.hankcs.hanlp.seg.Segment")
    Term = JClass("com.hankcs.hanlp.seg.common.Term")

    segment = HanLP.newSegment().enableJapaneseNameRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
