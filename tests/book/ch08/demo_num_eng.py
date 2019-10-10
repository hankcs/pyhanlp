# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-24 16:55
# 《自然语言处理入门》8.2.3 基于规则的数词英文识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *

from tests.book.ch03.ngram_segment import ViterbiSegment

CharType = JClass('com.hankcs.hanlp.dictionary.other.CharType')

segment = ViterbiSegment()
print(segment.seg("牛奶三〇〇克壹佰块"))
print(segment.seg("牛奶300克100块"))
print(segment.seg("牛奶300g100rmb"))
# 演示自定义字符类型
text = "牛奶300~400g100rmb"
print(segment.seg(text))
CharType.set('~', CharType.CT_NUM)
print(segment.seg(text))
