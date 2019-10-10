# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-03-21 21:22
# 《自然语言处理入门》1.6 开源工具
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *


def main():
    HanLP.Config.enableDebug()
    #  为了避免你等得无聊，开启调试模式说点什么:-)
    print(HanLP.segment("王国维和服务员"))


if __name__ == '__main__':
    main()
