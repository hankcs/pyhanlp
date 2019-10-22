# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-26 21:16
# 《自然语言处理入门》2.5 双数组字典树
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *


class DoubleArrayTrie(object):
    def __init__(self, dic: dict) -> None:
        m = JClass('java.util.TreeMap')()
        for k, v in dic.items():
            m[k] = v
        DoubleArrayTrie = JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')
        dat = DoubleArrayTrie(m)
        # 自jpype 0.7起，使用反射技术获取私有成员，等效于下列三句话
        # self.base = dat.base
        # self.check = dat.check
        # self.value = dat.v
        DoubleArrayTrie.class_.getDeclaredField('base').setAccessible(True)
        DoubleArrayTrie.class_.getDeclaredField('check').setAccessible(True)
        DoubleArrayTrie.class_.getDeclaredField('v').setAccessible(True)
        self.base = DoubleArrayTrie.class_.getDeclaredField('base').get(dat)
        self.check = DoubleArrayTrie.class_.getDeclaredField('check').get(dat)
        self.value = DoubleArrayTrie.class_.getDeclaredField('v').get(dat)

    @staticmethod
    def char_hash(c) -> int:
        return JClass('java.lang.Character')(c).hashCode()

    def transition(self, c, b) -> int:
        """
        状态转移
        :param c: 字符
        :param b: 初始状态
        :return: 转移后的状态，-1表示失败
        """
        p = self.base[b] + self.char_hash(c) + 1
        if self.base[b] == self.check[p]:
            return p
        else:
            return -1

    def __getitem__(self, key: str):
        b = 0
        for i in range(0, len(key)):  # len(key)次状态转移
            p = self.transition(key[i], b)
            if p is not -1:
                b = p
            else:
                return None

        p = self.base[b]  # 按字符'\0'进行状态转移
        n = self.base[p]  # 查询base
        if p == self.check[p] and n < 0:  # 状态转移成功且对应词语结尾
            index = -n - 1  # 取得字典序
            return self.value[index]
        return None


if __name__ == '__main__':
    dic = {'自然': 'nature', '自然人': 'human', '自然语言': 'language', '自语': 'talk	to oneself', '入门': 'introduction'}
    dat = DoubleArrayTrie(dic)
    assert dat['自然'] == 'nature'
    assert dat['自然语言'] == 'language'
    assert dat['不存在'] is None
