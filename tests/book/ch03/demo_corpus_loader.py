# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-06 12:51
# 《自然语言处理入门》3.3.1 加载语料库
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.test_utility import test_data_path

CorpusLoader = SafeJClass('com.hankcs.hanlp.corpus.document.CorpusLoader')


def my_cws_corpus():
    data_root = test_data_path()
    corpus_path = os.path.join(data_root, 'my_cws_corpus.txt')
    if not os.path.isfile(corpus_path):
        with open(corpus_path, 'w', encoding='utf-8') as out:
            out.write('''商品 和 服务
商品 和服 物美价廉
服务 和 货币''')
    return corpus_path


def load_cws_corpus(corpus_path):
    return CorpusLoader.convert2SentenceList(corpus_path)


if __name__ == '__main__':
    corpus_path = my_cws_corpus()
    sents = load_cws_corpus(corpus_path)
    for sent in sents:
        print(sent)
