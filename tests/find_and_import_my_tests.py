# -*- coding:utf-8 -*-
# 如果你没有能力设置PYTHONPATH的话，这里提供一个傻瓜办法。
# 这个文件演示如何傻瓜式解决 ModuleNotFoundError: No module named 'tests.test_utility'
# 将下列代码拷贝到报错的文件顶部即可，一定要是顶部！
import os
import sys

folders = os.path.abspath(__file__ if '__file__' in globals() else '.').split(os.path.sep)
try:
    index = folders.index('tests')
    # 将tests放入path中，并且排除IPython/extensions下面的tests
    sys.path = [os.path.sep.join(folders[:index])] + [x for x in sys.path if 'IPython' not in x]
    from tests.test_utility import ensure_data
except ValueError:
    print('找不到tests目录，请将本文件放到tests下的任意子目录中运行')
    exit(1)
