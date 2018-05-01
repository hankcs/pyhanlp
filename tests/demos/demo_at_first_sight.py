# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-28
from pyhanlp import *

def demo_at_first_sight():
    """第一个Demo，惊鸿一瞥

    >>> demo_at_first_sight()
    首次编译运行时，HanLP会自动构建词典缓存，请稍候……
    [你好/vl, ，/w, 欢迎/v, 使用/v, HanLP/nx, 汉语/gi, 处理/vn, 包/v, ！/w, 接下来/vl, 请/v, 从/p, 其他/rzv, Demo/nx, 中/f, 体验/v, HanLP/nx, 丰富/a, 的/ude1, 功能/n, ~/nx]
    """
    print("首次编译运行时，HanLP会自动构建词典缓存，请稍候……")
    #HanLP.Config.enableDebug()
    print(HanLP.segment(
            "你好，欢迎使用HanLP汉语处理包！接下来请从其他Demo中体验HanLP丰富的功能~"))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
