# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-06 13:19
# 《自然语言处理入门》3.3 训练
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from jpype import JString

from pyhanlp import *
from tests.book.ch03.demo_corpus_loader import my_cws_corpus
from tests.book.ch03.msr import msr_model
from tests.test_utility import test_data_path

NatureDictionaryMaker = SafeJClass('com.hankcs.hanlp.corpus.dictionary.NatureDictionaryMaker')
CorpusLoader = SafeJClass('com.hankcs.hanlp.corpus.document.CorpusLoader')
WordNet = JClass('com.hankcs.hanlp.seg.common.WordNet')
Vertex = JClass('com.hankcs.hanlp.seg.common.Vertex')
ViterbiSegment = JClass('com.hankcs.hanlp.seg.Viterbi.ViterbiSegment')
DijkstraSegment = JClass('com.hankcs.hanlp.seg.Dijkstra.DijkstraSegment')
CoreDictionary = LazyLoadingJClass('com.hankcs.hanlp.dictionary.CoreDictionary')
Nature = JClass('com.hankcs.hanlp.corpus.tag.Nature')


def train_bigram(corpus_path, model_path):
    sents = CorpusLoader.convert2SentenceList(corpus_path)
    for sent in sents:
        for word in sent:
            if word.label is None:
                word.setLabel("n")
    maker = NatureDictionaryMaker()
    maker.compute(sents)
    maker.saveTxtTo(model_path)  # tests/data/my_cws_model.txt


def load_bigram(model_path, verbose=True, ret_viterbi=True):
    HanLP.Config.CoreDictionaryPath = model_path + ".txt"  # unigram
    HanLP.Config.BiGramDictionaryPath = model_path + ".ngram.txt"  # bigram
    # 以下部分为兼容新标注集，不感兴趣可以跳过
    HanLP.Config.CoreDictionaryTransformMatrixDictionaryPath = model_path + ".tr.txt"  # 词性转移矩阵，分词时可忽略
    if model_path != msr_model:
        with open(HanLP.Config.CoreDictionaryTransformMatrixDictionaryPath, encoding='utf-8') as src:
            for tag in src.readline().strip().split(',')[1:]:
                Nature.create(tag)
    CoreBiGramTableDictionary = SafeJClass('com.hankcs.hanlp.dictionary.CoreBiGramTableDictionary')
    CoreDictionary.getTermFrequency("商品")
    # 兼容代码结束
    if verbose:
        print(CoreDictionary.getTermFrequency("商品"))
        print(CoreBiGramTableDictionary.getBiFrequency("商品", "和"))
        sent = '商品和服务'
        # sent = '货币和服务'
        wordnet = generate_wordnet(sent, CoreDictionary.trie)
        print(wordnet)
        print(viterbi(wordnet))
    return ViterbiSegment().enableAllNamedEntityRecognize(False).enableCustomDictionary(
        False) if ret_viterbi else DijkstraSegment().enableAllNamedEntityRecognize(False).enableCustomDictionary(False)


def generate_wordnet(sent, trie):
    """
    生成词网
    :param sent: 句子
    :param trie: 词典（unigram）
    :return: 词网
    """
    searcher = trie.getSearcher(JString(sent), 0)
    wordnet = WordNet(sent)
    while searcher.next():
        wordnet.add(searcher.begin + 1,
                    Vertex(sent[searcher.begin:searcher.begin + searcher.length], searcher.value, searcher.index))
    # 原子分词，保证图连通
    vertexes = wordnet.getVertexes()
    i = 0
    while i < len(vertexes):
        if len(vertexes[i]) == 0:  # 空白行
            j = i + 1
            for j in range(i + 1, len(vertexes) - 1):  # 寻找第一个非空行 j
                if len(vertexes[j]):
                    break
            wordnet.add(i, Vertex.newPunctuationInstance(sent[i - 1: j - 1]))  # 填充[i, j)之间的空白行
            i = j
        else:
            i += len(vertexes[i][-1].realWord)

    return wordnet


def viterbi(wordnet):
    nodes = wordnet.getVertexes()
    # 前向遍历
    for i in range(0, len(nodes) - 1):
        for node in nodes[i]:
            for to in nodes[i + len(node.realWord)]:
                to.updateFrom(node)  # 根据距离公式计算节点距离，并维护最短路径上的前驱指针from
    # 后向回溯
    path = []  # 最短路径
    f = nodes[len(nodes) - 1].getFirst()  # 从终点回溯
    while f:
        path.insert(0, f)
        f = f.getFrom()  # 按前驱指针from回溯
    return [v.realWord for v in path]


if __name__ == '__main__':
    corpus_path = my_cws_corpus()
    model_path = os.path.join(test_data_path(), 'my_cws_model')
    train_bigram(corpus_path, model_path)
    load_bigram(model_path)
