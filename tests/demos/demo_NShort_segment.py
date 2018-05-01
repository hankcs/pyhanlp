# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30
from pyhanlp import *


def demo_NShort_segment(sentences):
    """ N最短路径分词，该分词器比最短路分词器慢，但是效果稍微好一些，对命名实体识别能力更强

    >>> sentences = [
    ...    "今天，刘志军案的关键人物,山西女商人丁书苗在市二中院出庭受审。",
    ...    "江西省监狱管理局与中国太平洋财产保险股份有限公司南昌中心支公司保险合同纠纷案",
    ...    "新北商贸有限公司",
    ...    ]
    >>> demo_NShort_segment(sentences)
    N-最短分词：[今天/t, ，/w, 刘志军/nr, 案/ng, 的/ude1, 关键/n, 人物/n, ,/w, 山西/ns,
        女/b, 商人/nnt, 丁书苗/nr, 在/p, 市/n, 二/m, 中/f, 院/n, 出庭/vi, 受审/vi, 。/w]
    最短路分词：[今天/t, ，/w, 刘志军/nr, 案/ng, 的/ude1, 关键/n, 人物/n, ,/w, 山西/ns,
        女/b, 商人/nnt, 丁书苗/nr, 在/p, 市/n, 二/m, 中/f, 院/n, 出庭/vi, 受审/vi, 。/w]
    N-最短分词：[江西省监狱管理局/nt, 与/cc, 中国/ns, 太平洋/ns, 财产/n, 保险/n, 股份/n,
        有限公司/nis, 南昌/ns, 中心支公司/nt, 保险/n, 合同/n, 纠纷案/nz]
    最短路分词：[江西省监狱管理局/nt, 与/cc, 中国/ns, 太平洋/ns, 财产/n, 保险/n, 股份/n,
        有限公司/nis, 南昌/ns, 中心支公司/nt, 保险/n, 合同/n, 纠纷案/nz]
    N-最短分词：[新北商贸有限公司/nt]
    最短路分词：[新北商贸有限公司/nt]
    """
    NShortSegment = JClass("com.hankcs.hanlp.seg.NShort.NShortSegment")
    Segment = JClass("com.hankcs.hanlp.seg.Segment")
    ViterbiSegment = JClass("com.hankcs.hanlp.seg.Viterbi.ViterbiSegment")

    nshort_segment = NShortSegment().enableCustomDictionary(False).enablePlaceRecognize(
        True).enableOrganizationRecognize(True)
    shortest_segment = ViterbiSegment().enableCustomDictionary(
        False).enablePlaceRecognize(True).enableOrganizationRecognize(True)

    for sentence in sentences:
        print("N-最短分词：{} \n最短路分词：{}".format(
            nshort_segment.seg(sentence), shortest_segment.seg(sentence)))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
