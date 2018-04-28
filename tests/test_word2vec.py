# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-04-28 10:07
import zipfile

from pyhanlp import *
from pyhanlp.static import download

if not os.path.isdir('tests/data/'):
    print('请在项目根目录下运行本脚本')
    exit(1)

if not os.path.isdir('tests/data/hanlp-wiki-vec-zh'):
    model_path = 'tests/data/hanlp-wiki-vec-zh.zip'
    download('http://hanlp.linrunsoft.com/release/model/hanlp-wiki-vec-zh.zip', model_path)
    with zipfile.ZipFile(model_path, "r") as archive:
        archive.extractall('tests/data/')

WordVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.WordVectorModel')
DocVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.DocVectorModel')
word2vec = WordVectorModel('tests/data/hanlp-wiki-vec-zh/hanlp-wiki-vec-zh.txt')
doc2vec = DocVectorModel(word2vec)
docs = ["山东苹果丰收", "农民在江苏种水稻", "奥运会女排夺冠", "世界锦标赛胜出", "中国足球失败"]
for idx, doc in enumerate(docs):
    doc2vec.addDocument(idx, doc)

print(word2vec.nearest('语言'))

for res in doc2vec.nearest('我要看比赛'):
    print('%s = %.2f' % (docs[res.getKey().intValue()], res.getValue().floatValue()))
