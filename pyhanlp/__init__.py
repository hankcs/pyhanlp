# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-18 19:49
import os
from jpype import *

from pyhanlp.static import HANLP_JAR_PATH, STATIC_ROOT

# 启动JVM
startJVM(getDefaultJVMPath(), "-Djava.class.path={}{}{}".format(HANLP_JAR_PATH, os.pathsep, STATIC_ROOT), "-Xms1g",
         "-Xmx1g")

# API列表
HanLP = JClass('com.hankcs.hanlp.HanLP')  # HanLP工具类
PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
