# # -*- coding:utf-8 -*-
# Author：wancong
# Date: 2018-04-30

# 在import pyhanlp之前编译自己的Java class，并放入pyhanlp/static中
import os

from pyhanlp.static import STATIC_ROOT, HANLP_JAR_PATH

java_code_path = os.path.join(STATIC_ROOT, 'MyFilter.java')
with open(java_code_path, 'w') as out:
    java_code = """
import com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary;
import com.hankcs.hanlp.dictionary.stopword.Filter;
import com.hankcs.hanlp.seg.common.Term;

public class MyFilter implements Filter
{
    public boolean shouldInclude(Term term)
    {
        if (term.nature.startsWith('m')) return true; // 数词保留
        return !CoreStopWordDictionary.contains(term.word); // 停用词过滤
    }
}
"""
    out.write(java_code)
os.system('javac -cp {} {} -d {}'.format(HANLP_JAR_PATH, java_code_path, STATIC_ROOT))
# 编译结束才可以启动hanlp
from pyhanlp import *


def demo_stopword():
    """

    >>> demo_stopword()
    [小区/n, 反对/v, 喂养/v, 流浪猫/nz, 赞成/v, 喂养/v, 小宝贝/nz]
    [小区/n, 居民/n, 反对/v, 喂养/v, 流浪猫/nz, 居民/n, 赞成/v, 喂养/v, 小宝贝/nz]
    [小区/n, 居民/n, 有/vyou, 的/ude1, 反对/v, 喂养/v, 流浪猫/nz, ，/w, 而/cc, 有的/rz, 居民/n, 却/d, 赞成/v, 喂养/v, 这些/rz, 小宝贝/nz]
    [小区/n, 居民/n, 反对/v, 喂养/v, 流浪猫/nz, 居民/n, 赞成/v, 喂养/v, 小宝贝/nz]
    [数字/n, 123/m, 保留/v]
    """
    CoreStopWordDictionary = JClass("com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary")
    Filter = JClass("com.hankcs.hanlp.dictionary.stopword.Filter")
    Term = JClass("com.hankcs.hanlp.seg.common.Term")
    BasicTokenizer = JClass("com.hankcs.hanlp.tokenizer.BasicTokenizer")
    NotionalTokenizer = JClass("com.hankcs.hanlp.tokenizer.NotionalTokenizer")

    text = "小区居民有的反对喂养流浪猫，而有的居民却赞成喂养这些小宝贝"
    # 可以动态修改停用词词典
    CoreStopWordDictionary.add("居民")
    print(NotionalTokenizer.segment(text))
    CoreStopWordDictionary.remove("居民")
    print(NotionalTokenizer.segment(text))

    # 可以对任意分词器的结果执行过滤
    term_list = BasicTokenizer.segment(text)
    print(term_list)
    CoreStopWordDictionary.apply(term_list)
    print(term_list)

    # 还可以自定义过滤逻辑
    MyFilter = JClass('MyFilter')
    CoreStopWordDictionary.FILTER = MyFilter()
    print(NotionalTokenizer.segment("数字123的保留"))  # “的”位于stopwords.txt所以被过滤，数字得到保留


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
