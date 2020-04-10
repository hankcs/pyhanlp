# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-30 21:03
# 《自然语言处理入门》9.1 新词提取
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from tests.test_utility import ensure_data

HLM_PATH = ensure_data("红楼梦.txt", "http://file.hankcs.com/corpus/红楼梦.zip")
XYJ_PATH = ensure_data("西游记.txt", "http://file.hankcs.com/corpus/西游记.zip")
SHZ_PATH = ensure_data("水浒传.txt", "http://file.hankcs.com/corpus/水浒传.zip")
SAN_PATH = ensure_data("三国演义.txt", "http://file.hankcs.com/corpus/三国演义.zip")
WEIBO_PATH = ensure_data("weibo-classification", "http://file.hankcs.com/corpus/weibo-classification.zip")


def test_weibo():
    for folder in os.listdir(WEIBO_PATH):
        print(folder)
        big_text = ""
        for file in os.listdir(os.path.join(WEIBO_PATH, folder)):
            with open(os.path.join(WEIBO_PATH, folder, file), encoding='utf-8') as src:
                big_text += "".join(src.readlines())
        word_info_list = HanLP.extractWords(big_text, 100)
        print(word_info_list)


def extract(corpus):
    print("%s 热词" % corpus)
    word_info_list = HanLP.extractWords(IOUtil.newBufferedReader(corpus), 100)
    print(word_info_list)
    # print("%s 新词" % corpus)
    # word_info_list = HanLP.extractWords(IOUtil.newBufferedReader(corpus), 100, True)
    # print(word_info_list)


if __name__ == '__main__':
    extract(HLM_PATH)
    extract(XYJ_PATH)
    extract(SHZ_PATH)
    extract(SAN_PATH)
    test_weibo()

    # 更多参数
    word_info_list = HanLP.extractWords(IOUtil.newBufferedReader(HLM_PATH), 100, True, 4, 0.0, .5, 100)
    print(word_info_list)
