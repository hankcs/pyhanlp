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
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse, quote

from pyhanlp import HanLP
from pyhanlp.static import INDEX_HTML

SENTENCE = 'sentence'
TEMPLATE = 'Error'
with open(INDEX_HTML) as src:
    TEMPLATE = src.read()


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
        sentence = 'HanLP是面向生产环境的自然语言处理工具包。'
        if SENTENCE in params:
            s = params[SENTENCE]
            if len(s):
                sentence = s[0].strip()
        MAX_LENGTH = 200
        if len(sentence) > MAX_LENGTH:
            sentence = sentence[:MAX_LENGTH]
        conll = quote(HanLP.parseDependency(sentence).__str__())
        self.write(TEMPLATE.replace('{SENTENCE}', sentence).replace('{CONLL}', conll))

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
