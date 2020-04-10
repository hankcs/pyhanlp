# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-01 09:53
# 《自然语言处理入门》2.1.2 词的性质——齐夫定律
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
import os
from collections import Counter

import numpy as np

from tests.test_utility import ensure_data

sighan05 = ensure_data('icwb2-data', 'http://sighan.cs.uchicago.edu/bakeoff2005/data/icwb2-data.zip')
msr = os.path.join(sighan05, 'training', 'msr_training.utf8')

f = Counter()
with open(msr, encoding='utf-8') as src:
    for line in src:
        line = line.strip()
        for word in line.split('  '):
            # word = word.strip()
            # if len(word) < 2: continue
            f[word] += 1


def plot(token_counts, title='MSR语料库词频统计', ylabel='词频'):
    from matplotlib import pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    fig = plt.figure(
        # figsize=(8, 6)
    )
    ax = fig.add_subplot(111)
    token_counts = list(zip(*token_counts))
    num_elements = np.arange(len(token_counts[0]))
    top_offset = max(token_counts[1]) + len(str(max(token_counts[1])))
    ax.set_title(title)
    ax.set_xlabel('词语')
    ax.set_ylabel(ylabel)
    ax.xaxis.set_label_coords(1.05, 0.015)
    ax.set_xticks(num_elements)
    ax.set_xticklabels(token_counts[0], rotation=55, verticalalignment='top')
    ax.set_ylim([0, top_offset])
    ax.set_xlim([-1, len(token_counts[0])])
    rects = ax.plot(num_elements, token_counts[1], linewidth=1.5)
    plt.show()


word_freq = f.most_common(30)
print(word_freq)
plot(word_freq)
# log_word_freq = []
# for w, f in word_freq:
#     log_word_freq.append((w, np.log(f)))
# plot(log_word_freq, ylabel='词频的对数')
