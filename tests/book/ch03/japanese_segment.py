# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-07 18:37
# 《自然语言处理入门》3.6.1 日语分词语料
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
import os

from tests.book.ch03.ngram_segment import train_bigram, load_bigram
from tests.test_utility import ensure_data

jp_corpus = ensure_data('jpcorpus',
                        'http://file.hankcs.com/corpus/jpcorpus.zip')
jp_bigram = os.path.join(jp_corpus, 'jp_bigram')
jp_corpus = os.path.join(jp_corpus, 'ja_gsd-ud-train.txt')

if __name__ == '__main__':
    train_bigram(jp_corpus, jp_bigram)  # 训练
    segment = load_bigram(jp_bigram, verbose=False)  # 加载
    print(segment.seg('自然言語処理入門という本が面白いぞ！'))  # 日语分词
