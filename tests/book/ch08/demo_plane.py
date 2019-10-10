# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-29 23:24
# 《自然语言处理入门》8.6 自定义领域命名实体识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from tests.book.ch05.perceptron_cws import CWSTrainer
from tests.book.ch07.demo_hmm_pos import AbstractLexicalAnalyzer, PerceptronSegmenter
from tests.book.ch07.demo_perceptron_pos import PerceptronPOSTagger
from tests.book.ch08.demo_sp_ner import NERTrainer, os, PerceptronNERecognizer
from tests.test_utility import ensure_data

PLANE_ROOT = ensure_data("plane-re", "http://file.hankcs.com/corpus/plane-re.zip")
PLANE_CORPUS = os.path.join(PLANE_ROOT, 'train.txt')
PLANE_MODEL = os.path.join(PLANE_ROOT, 'model.bin')

if __name__ == '__main__':
    trainer = NERTrainer()
    trainer.tagSet.nerLabels.clear()  # 不识别nr、ns、nt
    trainer.tagSet.nerLabels.add("np")  # 目标是识别np
    recognizer = PerceptronNERecognizer(trainer.train(PLANE_CORPUS, PLANE_MODEL).getModel())
    # 在NER预测前，需要一个分词器，最好训练自同源语料库
    CWS_MODEL = CWSTrainer().train(PLANE_CORPUS, PLANE_MODEL.replace('model.bin', 'cws.bin')).getModel()
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(CWS_MODEL), PerceptronPOSTagger(), recognizer)
    print(analyzer.analyze("米高扬设计米格-17PF：米格-17PF型战斗机比米格-17P性能更好。"))
    print(analyzer.analyze("米格-阿帕奇-666S横空出世。"))
