# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2021-04-21 12:33

# 在import pyhanlp之前编译如下的Java class，并放入pyhanlp/static中
# MultiThreadSegment运行于JVM，不受限于GIL，比Python多线程更快
# 在线运行：https://play.hanlp.ml/run/pyhanlp-multi-thread
import os
from pyhanlp.static import STATIC_ROOT, HANLP_JAR_PATH

assert os.system('javac -version') == 0, '编译需要安装JDK，内含编译器javac。例如，conda install -c conda-forge openjdk'
java_code_path = os.path.join(STATIC_ROOT, 'MultiThreadSegment.java')
with open(java_code_path, 'w') as out:
    java_code = """
import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.seg.common.Term;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class MultiThreadSegment
{
    public static class Job implements Callable<List<Term>>
    {
        private final String text;

        public Job(String text)
        {
            this.text = text;
        }

        @Override
        public List<Term> call()
        {
            return HanLP.segment(text); // 你可以修改这里调用其它功能，注意同步替换返回类型List<Term>
        }
    }

    public static List<List<Term>> segment(String[] sentences, int nThreads) throws ExecutionException, InterruptedException
    {
        ExecutorService executor = Executors.newFixedThreadPool(nThreads);
        List<List<Term>> results = new ArrayList<>(sentences.length);
        List<Future<List<Term>>> futureList = new ArrayList<>(sentences.length);
        for (String sentence : sentences)
        {
            futureList.add(executor.submit(new Job(sentence)));
        }
        for (Future<List<Term>> future : futureList)
        {
            results.add(future.get());
        }
        executor.shutdown();
        return results;
    }

    public static List<List<Term>> segment(String[] sentences) throws ExecutionException, InterruptedException
    {
        return segment(sentences, Runtime.getRuntime().availableProcessors());
    }
}
"""
    out.write(java_code)
assert os.system('javac -cp {} {} -d {}'.format(HANLP_JAR_PATH, java_code_path, STATIC_ROOT)) == 0, '编译失败，请检查Java语法'
# 编译结束才可以启动hanlp
from pyhanlp import *

MultiThreadSegment = JClass('MultiThreadSegment')
sentences = ['商品和服务'] * 1024
print(MultiThreadSegment.segment(sentences))
