# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-24 21:23
# 《自然语言处理入门》2.3.4 双向最长匹配
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from tests.book.ch02.backward_segment import backward_segment
from tests.book.ch02.forward_segment import forward_segment
from tests.book.ch02.utility import load_dictionary


def count_single_char(word_list: list):  # 统计单字成词的个数
    return sum(1 for word in word_list if len(word) == 1)


def bidirectional_segment(text, dic):
    f = forward_segment(text, dic)
    b = backward_segment(text, dic)
    if len(f) < len(b):                                  # 词数更少优先级更高
        return f
    elif len(f) > len(b):
        return b
    else:
        if count_single_char(f) < count_single_char(b):  # 单字更少优先级更高
            return f
        else:
            return b                                     # 都相等时逆向匹配优先级更高


if __name__ == '__main__':
    dic = load_dictionary()

    print(bidirectional_segment('研究生命起源', dic))