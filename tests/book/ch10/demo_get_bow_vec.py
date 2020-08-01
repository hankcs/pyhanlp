# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-07-31 20:55
# 《自然语言处理入门》第 10 章 文本聚类 （这段代码来自书籍之外的附赠答疑）
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

import os

from pyhanlp.static import STATIC_ROOT, HANLP_JAR_PATH

java_code_path = os.path.join(STATIC_ROOT, 'MyClusterAnalyzer.java')
with open(java_code_path, 'w') as out:
    java_code = """
import com.hankcs.hanlp.mining.cluster.ClusterAnalyzer;
import com.hankcs.hanlp.mining.cluster.SparseVector;

public class MyClusterAnalyzer<K> extends ClusterAnalyzer<K>
{
    public SparseVector toVector(String document)
    {
        return toVector(preprocess(document));
    }
}
"""
    out.write(java_code)
os.system('javac -cp {} {} -d {}'.format(HANLP_JAR_PATH, java_code_path, STATIC_ROOT))
# 编译结束才可以启动hanlp
from pyhanlp import *

ClusterAnalyzer = JClass('MyClusterAnalyzer')

if __name__ == '__main__':
    analyzer = ClusterAnalyzer()
    vec = analyzer.toVector("古典, 古典, 古典, 古典, 古典, 古典, 古典, 古典, 摇滚")
    print(vec)
    # print(analyzer.kmeans(3))
    # print(analyzer.repeatedBisection(3))
    # print(analyzer.repeatedBisection(1.0))  # 自动判断聚类数量k
