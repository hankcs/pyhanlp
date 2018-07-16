# -*- coding:utf-8 -*-
# Filename: server.py
# Author：hankcs
# Date: 2018-03-03 下午9:47

"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
import os
import random
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse, quote

from pyhanlp import HanLP, JClass
from pyhanlp.static import INDEX_HTML

SENTENCE = 'sentence'
TEMPLATE = 'Error'
HANLP_GOOGLE_UA = 'UA-XXXXX-X'
ENVIRON = os.environ.copy()
if "HANLP_GOOGLE_UA" in ENVIRON:
    HANLP_GOOGLE_UA = ENVIRON["HANLP_GOOGLE_UA"]
with open(INDEX_HTML, encoding='utf-8') as src:
    TEMPLATE = src.read()
lexical_analyzer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer').ANALYZER


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def write(self, text: str):
        self.wfile.write(text.encode())

    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        self._set_headers()
        # {'text': ['I looove iparser!']}
        titles = ['HanLP是面向生产环境的自然语言处理工具包。',
                  '上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美国纽约现代艺术博物馆参观。',
                  # '词法分析包括中文分词、词性标注和命名实体识别。',
                  # '本页面词法分析采用的是感知机算法。',
                  '剑桥分析公司多位高管对卧底记者说，他们确保了唐纳德·特朗普在总统大选中获胜。',
                  '收件人在万博·齐都国际绿茵花园（东门）A8栋，靠近泰山护理职业学院。',
                  # '双桥街道双桥社区劳动和社会保障工作站地址是扬州市四望亭路293号双桥村4楼。',
                  '他在浙江金华出生，他的名字叫金华。',
                  '总统普京与特朗普通电话讨论美国太空探索技术公司。',
                  '云南丽江多措并举推进“河长制”取得实效',
                  '微软公司於1975年由比爾·蓋茲和保羅·艾倫創立，18年啟動以智慧雲端、前端為導向的大改組。',
                  '北京大学计算语言学研究所和富士通研究开发中心有限公司，得到了人民日报社新闻信息中心的语料库。',
                  # '可以自由设置句法分析模块中的分词算法。',
                  # '敬请注意本页面不接受过长的句子。',
                  # '徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。',
                  '萨哈夫说，伊拉克将同联合国销毁伊拉克大规模杀伤性武器特别委员会继续保持合作。',
                  '中央人民政府驻澳门特别行政区联络办公室的张朝阳说商品和服务是三原县鲁桥食品厂的主营业务。']
        sentence = random.choice(titles)
        if SENTENCE in params:
            s = params[SENTENCE]
            if len(s):
                sentence = s[0].strip()
        punctuation = re.compile('[。！？!?]')
        sentence = sentence[:len(punctuation.split(sentence)[0]) + 1]
        sentence = sentence.replace(' ', '')
        MAX_LENGTH = 50
        if len(sentence) > MAX_LENGTH:
            sentence = '请输入{}字以内的句子'.format(MAX_LENGTH)
        ann = '词法分析可视化仅支持 HanLP 1.6.2及以上版本'
        if lexical_analyzer:
            ann = lexical_analyzer.analyze(sentence).translateCompoundWordLabels().toStandoff(True).__str__()
        conll = HanLP.parseDependency(sentence).__str__()
        self.write(TEMPLATE.replace('{SENTENCE}', sentence).replace('{CONLL}', quote(conll))
                   .replace('{HANLP_GOOGLE_UA}', HANLP_GOOGLE_UA, 1)
                   .replace('{ANN}', quote(ann))
                   )

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.write("<html><body><h1>POST!</h1></body></html>")


def run(server_class=HTTPServer, handler_class=S, port=8765):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('服务器已启动 http://localhost:{}'.format(port))
    httpd.serve_forever()
