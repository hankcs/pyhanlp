# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-02-26 19:59
# 《自然语言处理入门》13.3 word2vec
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from pyhanlp import *
from tests.book.ch03.msr import msr_train
from tests.test_utility import test_data_path

IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')
DocVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.DocVectorModel')
Word2VecTrainer = JClass('com.hankcs.hanlp.mining.word2vec.Word2VecTrainer')
WordVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.WordVectorModel')

# 演示词向量的训练与应用
TRAIN_FILE_NAME = msr_train
MODEL_FILE_NAME = os.path.join(test_data_path(), "word2vec.txt")


def print_nearest(word, model):
    print(
        "\n                                                Word     "
        "Cosine\n------------------------------------------------------------------------")
    for entry in model.nearest(word):
        print("%50s\t\t%f" % (entry.getKey(), entry.getValue()))


def print_nearest_document(document, documents, model):
    print_header(document)
    for entry in model.nearest(document):
        print("%50s\t\t%f" % (documents[entry.getKey()], entry.getValue()))


def print_header(query):
    print(
        "\n%50s          Cosine\n------------------------------------------------------------------------" % (query))


def train_or_load_model():
    if not IOUtil.isFileExisted(MODEL_FILE_NAME):
        if not IOUtil.isFileExisted(TRAIN_FILE_NAME):
            raise RuntimeError("语料不存在，请阅读文档了解语料获取与格式：https://github.com/hankcs/HanLP/wiki/word2vec")
        trainerBuilder = Word2VecTrainer();
        return trainerBuilder.train(TRAIN_FILE_NAME, MODEL_FILE_NAME)
    return load_model()


def load_model():
    return WordVectorModel(MODEL_FILE_NAME)


if __name__ == '__main__':
    wordVectorModel = train_or_load_model()
    print_nearest("上海", wordVectorModel)
    print_nearest("美丽", wordVectorModel)
    print_nearest("购买", wordVectorModel)
    print(wordVectorModel.similarity("上海", "广州"))
    print(wordVectorModel.analogy("日本", "自民党", "共和党"))
    #  文档向量
    docVectorModel = DocVectorModel(wordVectorModel)
    documents = ["山东苹果丰收",
                 "农民在江苏种水稻",
                 "奥运会女排夺冠",
                 "世界锦标赛胜出",
                 "中国足球失败", ]
    print(docVectorModel.similarity("山东苹果丰收", "农民在江苏种水稻"))
    print(docVectorModel.similarity("山东苹果丰收", "世界锦标赛胜出"))
    print(docVectorModel.similarity(documents[0], documents[1]))
    print(docVectorModel.similarity(documents[0], documents[4]))
    for i, d in enumerate(documents):
        docVectorModel.addDocument(i, documents[i])
    print_nearest_document("体育", documents, docVectorModel)
    print_nearest_document("农业", documents, docVectorModel)
    print_nearest_document("我要看比赛", documents, docVectorModel)
    print_nearest_document("要不做饭吧", documents, docVectorModel)
