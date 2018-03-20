# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-18 19:49
from __future__ import print_function
from __future__ import division

import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, os.path.pardir))

PY = 3
if sys.version_info[0] < 3:
    PY = 2
    # noinspection PyUnresolvedReferences
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

# Get ENV
ENVIRON = os.environ.copy()

import os
from jpype import *


'''
Load variables in Environment
'''
if "HANLP_STATIC_ROOT" in ENVIRON:
    STATIC_ROOT = ENVIRON["HANLP_STATIC_ROOT"]
else:
    from pyhanlp.static import STATIC_ROOT

if "HANLP_JAR_PATH" in ENVIRON:
    HANLP_JAR_PATH = ENVIRON["HANLP_JAR_PATH"]
else:
    from pyhanlp.static import HANLP_JAR_PATH

if "HANLP_JVM_XMS" in ENVIRON:
    HANLP_JVM_XMS = ENVIRON["HANLP_JVM_XMS"]
else:
    HANLP_JVM_XMS = "1g"

if "HANLP_JVM_XMX" in ENVIRON:
    HANLP_JVM_XMX = ENVIRON["HANLP_JVM_XMX"]
else:
    HANLP_JVM_XMX = "1g"

if os.path.exists(HANLP_JAR_PATH) and os.path.exists(STATIC_ROOT):
    pass  # 调试输出会干扰pipeline
    # print("加载 HanLP jar [%s] ..." % HANLP_JAR_PATH)
    # print("加载 HanLP config [%s/hanlp.properties] ..." % (STATIC_ROOT))
    # print("加载 HanLP data [%s/data] ..." % (STATIC_ROOT))
else:
    raise BaseException(
        "Error: %s or %s does not exists." %
        (HANLP_JAR_PATH, STATIC_ROOT))

JAVA_JAR_CLASSPATH = "-Djava.class.path=%s%s%s" % (
    HANLP_JAR_PATH, os.pathsep, STATIC_ROOT)
# print("设置 JAVA_JAR_CLASSPATH [%s]" % JAVA_JAR_CLASSPATH)
# JAVA_JAR_CLASSPATH="-Djava.class.path=/pyhanlp/jars/hanlp-portable-1.6.0.jar"
# 启动JVM
startJVM(
    getDefaultJVMPath(),
    JAVA_JAR_CLASSPATH,
    "-Xms%s" %
    HANLP_JVM_XMS,
    "-Xmx%s" %
    HANLP_JVM_XMX)

# API列表
HanLP = JClass('com.hankcs.hanlp.HanLP')  # HanLP工具类
PerceptronLexicalAnalyzer = JClass(
    'com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
