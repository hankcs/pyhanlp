# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-02-26 15:16
# 《自然语言处理入门》13.2 深度学习与优势
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from matplotlib import pylab as plt
import numpy as np

sigmoid = lambda x: 1 / (1 + np.exp(-x))

x = plt.linspace(-10, 10, 10000)

plt.plot(x, sigmoid(x), 'b')
plt.grid()

plt.title(r'$\sigma(x)=\frac{1}{1+e^{-x}}$')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('sigmoid.png')
plt.show()
