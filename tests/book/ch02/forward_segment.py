# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-22 21:05
# 《自然语言处理入门》2.3.2 正向最长匹配
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from tests.book.ch02.utility import load_dictionary


def forward_segment(text, dic):
    word_list = []
    i = 0
    while i < len(text):
        longest_word = text[i]                      # 当前扫描位置的单字
        for j in range(i + 1, len(text) + 1):       # 所有可能的结尾
            word = text[i:j]                        # 从当前位置到结尾的连续字符串
            if word in dic:                         # 在词典中
                if len(word) > len(longest_word):   # 并且更长
                    longest_word = word             # 则更优先输出
        word_list.append(longest_word)              # 输出最长词
        i += len(longest_word)                      # 正向扫描
    return word_list


if __name__ == '__main__':
    dic = load_dictionary()

    print(forward_segment('就读北京大学', dic))
    print(forward_segment('研究生命起源', dic))
