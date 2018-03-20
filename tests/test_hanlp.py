# -*- coding:utf-8 -*-
# Author：hankcs, Hai Liang Wang<hailiang.hl.wang@gmail.com>
# Date: 2018-03-18 21:07
# 
from __future__ import print_function
from __future__ import division

import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, os.path.pardir))

from absl import flags   #absl-py
from absl import logging #absl-py
from absl import app #absl-py

#  支持调试日志
FLAGS = flags.FLAGS
FLAGS([__file__, '--verbosity', '1']) # DEBUG 1; INFO 0; WARNING -1; ERROR -2

import unittest
from pyhanlp import *

# run testcase: python /Users/hain/ai/textsum/app/py/classifier/preprocesser.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_keywords(self):
        logging.info("test_keywords")
        # 关键词提取
        document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
                   "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
                   "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
                   "严格地进行水资源论证和取水许可的批准。"
        print(HanLP.extractKeyword(document, 2))
        
    def test_textsum(self):
        logging.info("test_textsum")
        # 自动摘要
        document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
                   "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
                   "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
                   "严格地进行水资源论证和取水许可的批准。"
        print(HanLP.extractSummary(document, 3))
        # 依存句法分析
        
    def test_parsedependency(self):
        logging.info("test_parsedependency")
        logging.info(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))
        # 更底层的API需要参考Java语法用JClass引入更深的类路径

    def test_analyze(self):
        logging.info("test_analyze")
        analyzer = PerceptronLexicalAnalyzer()
        print(analyzer.analyze("上海华安工业（集团）公司董事长谭旭光和秘书胡花蕊来到美国纽约现代艺术博物馆参观"))
        # 任何模型总会有失误，特别是98年这种陈旧的语料库
        print(analyzer.analyze("总统普京与特朗普通电话讨论太空探索技术公司"))
        # 支持在线学习
        analyzer.learn("与/c 特朗普/nr 通/v 电话/n 讨论/v [太空/s 探索/vn 技术/n 公司/n]/nt")
        # 学习到新知识
        print(analyzer.analyze("总统普京与特朗普通电话讨论太空探索技术公司"))
        # 还可以举一反三
        print(analyzer.analyze("主席和特朗普通电话"))

        # 知识的泛化不是死板的规则，而是比较灵活的统计信息
        print(analyzer.analyze("我在浙江金华出生"))
        analyzer.learn("在/p 浙江/ns 金华/ns 出生/v")
        print(analyzer.analyze("我在四川金华出生"))
        print(analyzer.analyze("我的名字叫金华"))

    def test_segment(self):
        logging.info("test_segment")
        print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
        testCases = [
            "商品和服务",
            "结婚的和尚未结婚的确实在干扰分词啊",
            "买水果然后来世博园最后去世博会",
            "中国的首都是北京",
            "欢迎新老师生前来就餐",
            "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
            "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"]
        for sentence in testCases: print(HanLP.segment(sentence))

def test():
    unittest.main()

if __name__ == '__main__':
    test()


