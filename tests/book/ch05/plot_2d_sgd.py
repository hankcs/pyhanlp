# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-26 16:49
# 《自然语言处理入门》5.2.4 损失函数与随机梯度下降
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

import matplotlib.pyplot as plt
import numpy as np

from tests.book.ch05.plot_name import newline

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.linspace(-1.5, 1.5)
y = x ** 2

newline([1, 0], [1, 1], color='g')

plt.ylim([0, 2])

plt.plot(x, y)
plt.title('$J(w)=w^2$')
plt.xlabel('$w$')
plt.ylabel('$J(w)$')
plt.annotate('梯度$\Delta w = 2$', xy=(1, 1), xytext=(0, 1.0), ha='center',
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

bbox_props = dict(boxstyle="larrow", fc='w', ec="black", lw=2)
t = plt.text(0.6, 0.1, "梯度下降方向", ha="center", va="center", rotation=0,
             bbox=bbox_props)
bbox_props['boxstyle'] = 'rarrow'
plt.text(1.4, 0.1, "梯度上升方向", ha="center", va="center", rotation=0,
         bbox=bbox_props)

plt.show()
