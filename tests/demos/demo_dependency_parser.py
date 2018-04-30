# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-29
from pyhanlp import *


def demo_dependency_parser():
    """ 依存句法分析（CRF句法模型需要-Xms512m -Xmx512m -Xmn256m，
        MaxEnt和神经网络句法模型需要-Xms1g -Xmx1g -Xmn512m）

    >>> demo_dependency_parser()
    徐先生 --(主谓关系)--> 帮助
    还 --(状中结构)--> 帮助
    具体 --(状中结构)--> 帮助
    帮助 --(核心关系)--> ##核心##
    他 --(兼语)--> 帮助
    确定 --(动宾关系)--> 帮助
    了 --(右附加关系)--> 确定
    把 --(状中结构)--> 作为
    画 --(介宾关系)--> 把
    雄鹰 --(动宾关系)--> 画
    、 --(标点符号)--> 松鼠
    松鼠 --(并列关系)--> 雄鹰
    和 --(左附加关系)--> 麻雀
    麻雀 --(并列关系)--> 雄鹰
    作为 --(动宾关系)--> 确定
    主攻 --(定中关系)--> 目标
    目标 --(动宾关系)--> 作为
    。 --(标点符号)--> 帮助
    <BLANKLINE>
    徐先生 --(主谓关系)--> 帮助
    还 --(状中结构)--> 帮助
    具体 --(状中结构)--> 帮助
    帮助 --(核心关系)--> ##核心##
    他 --(兼语)--> 帮助
    确定 --(动宾关系)--> 帮助
    了 --(右附加关系)--> 确定
    把 --(状中结构)--> 作为
    画 --(介宾关系)--> 把
    雄鹰 --(动宾关系)--> 画
    、 --(标点符号)--> 松鼠
    松鼠 --(并列关系)--> 雄鹰
    和 --(左附加关系)--> 麻雀
    麻雀 --(并列关系)--> 雄鹰
    作为 --(动宾关系)--> 确定
    主攻 --(定中关系)--> 目标
    目标 --(动宾关系)--> 作为
    。 --(标点符号)--> 帮助
    <BLANKLINE>
    麻雀 --(并列关系)-->
    雄鹰 --(动宾关系)-->
    画 --(介宾关系)-->
    把 --(状中结构)-->
    作为 --(动宾关系)-->
    确定 --(动宾关系)-->
    帮助 --(核心关系)-->
    ##核心##
    """
    sentence = HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。")
    for word in sentence.iterator():  # 通过dir()可以查看sentence的方法
        print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
    print()

    # 也可以直接拿到数组，任意顺序或逆序遍历
    word_array = sentence.getWordArray()
    for word in word_array:
        print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
    print()

    # 还可以直接遍历子树，从某棵子树的某个节点一路遍历到虚根
    CoNLLWord = JClass("com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLWord")
    head = word_array[12]
    while head.HEAD:
        head = head.HEAD
        if (head == CoNLLWord.ROOT):
            print(head.LEMMA)
        else:
            print("%s --(%s)--> " % (head.LEMMA, head.DEPREL))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
