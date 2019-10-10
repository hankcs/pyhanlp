# 《自然语言处理入门》6.2.2 条件随机场的训练
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025
x = np.arange(-2.0, 2.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = -((X - 1) ** 2)
Z2 = -(Y ** 2)
Z = -1.0 * (Z2 + Z1) + 1

plt.figure()
CS = plt.contour(X, Y, Z)
plt.annotate('', xy=(0.05, 0.05), xycoords='axes fraction',
             xytext=(0.2, 0.2), textcoords='axes fraction',
             va="center", ha="center", bbox=leafNode, arrowprops=arrow_args)
plt.text(-1.85, -1.67, '$P_0$')

plt.annotate('', xy=(0.2, 0.2), xycoords='axes fraction',
             xytext=(0.35, 0.33), textcoords='axes fraction',
             va="center", ha="center", bbox=leafNode, arrowprops=arrow_args)
plt.text(-1.32, -1.23, '$P_1$')

plt.annotate('', xy=(0.35, 0.33), xycoords='axes fraction',
             xytext=(0.52, 0.43), textcoords='axes fraction',
             va="center", ha="center", bbox=leafNode, arrowprops=arrow_args)
plt.text(-0.7, -0.65, '$P_2$')

plt.annotate('', xy=(0.52, 0.43), xycoords='axes fraction',
             xytext=(0.75, 0.5), textcoords='axes fraction',
             va="center", ha="center", bbox=leafNode, arrowprops=arrow_args)
plt.text(0., -0.24, '$P_3$')
plt.text(0.95, -0.1, '$P_4$')

plt.annotate('', xy=(0.05, 0.05), xycoords='axes fraction',
             xytext=(0.75, 0.5), textcoords='axes fraction',
             va="center", ha="center", bbox=leafNode, arrowprops={"arrowstyle": "<-", 'ls': 'dashed'})

plt.xticks([])
plt.yticks([])
plt.clabel(CS, inline=1, fontsize=10)
plt.title('梯度下降')
plt.xlabel('$w_1$')
plt.ylabel('$w_2$')
plt.show()
