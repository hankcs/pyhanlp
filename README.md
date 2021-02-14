# pyhanlp: Python interfaces for HanLP1.x

![pypi](https://img.shields.io/pypi/v/pyhanlp) [![Downloads](https://pepy.tech/badge/pyhanlp)](https://pepy.tech/project/pyhanlp) [![GitHub license](https://img.shields.io/github/license/hankcs/pyhanlp)](https://github.com/hankcs/pyhanlp/blob/master/LICENSE)

[HanLP1.x](https://github.com/hankcs/HanLP/tree/1.x)的Python接口，支持自动下载与升级[HanLP1.x](https://github.com/hankcs/HanLP/tree/1.x)，兼容py2、py3。内部算法经过工业界和学术界考验，配套书籍[《自然语言处理入门》](http://nlp.hankcs.com/book.php)已经出版，欢迎查阅[随书代码](https://github.com/hankcs/pyhanlp/tree/master/tests/book)。基于深度学习的[HanLP2.x](https://github.com/hankcs/HanLP/tree/doc-zh)已于2020年初发布，次世代最先进的多语种NLP技术，与1.x相辅相成，平行发展。

## 安装

**非IT人士**可直接使用[傻瓜虚拟机](https://od.hankcs.com/book/intro_nlp/%E5%82%BB%E7%93%9C%E8%99%9A%E6%8B%9F%E6%9C%BA/)；**新手**建议观看[安装教程（附安装包）](https://od.hankcs.com/book/intro_nlp/%E5%AE%89%E8%A3%85%E5%8C%85/)；**工程师**请：

先安装[JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)和[Python<=3.8](https://docs.conda.io/en/latest/miniconda.html)。要求JDK、操作系统和Python位数一致。然后[设置JAVA_HOME环境变量](https://bbs.hankcs.com/t/hanlp-java/999)，最后执行：

```bash
conda install -c conda-forge jpype1==0.7.0      # (可选)conda安装jpype1更方便
pip install pyhanlp
```

使用命令`hanlp`来验证安装，如因网络等原因自动安装失败，可参考[手动配置](https://github.com/hankcs/pyhanlp/wiki/%E6%89%8B%E5%8A%A8%E9%85%8D%E7%BD%AE)或[Windows指南](https://github.com/hankcs/pyhanlp/wiki/Windows)。

## 命令行

### 中文分词

使用命令`hanlp segment`进入交互分词模式，输入一个句子并回车，[HanLP1.x](https://github.com/hankcs/HanLP/tree/1.x)会输出分词结果：

```python
$ hanlp segment
商品和服务
商品/n 和/cc 服务/vn
当下雨天地面积水分外严重
当/p 下雨天/n 地面/n 积水/n 分外/d 严重/a
龚学平等领导说,邓颖超生前杜绝超生
龚学平/nr 等/udeng 领导/n 说/v ,/w 邓颖超/nr 生前/t 杜绝/v 超生/vi
```

还可以重定向输入输出到文件等：

```python
$ hanlp segment <<< '欢迎新老师生前来就餐'               
欢迎/v 新/a 老/a 师生/n 前来/vi 就餐/vi
```

### 依存句法分析

命令为`hanlp parse`，同样支持交互模式和重定向：

```python
$ hanlp parse <<< '徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。'         
1	徐先生	徐先生	nh	nr	_	4	主谓关系	_	_
2	还	还	d	d	_	4	状中结构	_	_
3	具体	具体	a	a	_	4	状中结构	_	_
4	帮助	帮助	v	v	_	0	核心关系	_	_
5	他	他	r	rr	_	4	兼语	_	_
6	确定	确定	v	v	_	4	动宾关系	_	_
7	了	了	u	ule	_	6	右附加关系	_	_
8	把	把	p	pba	_	15	状中结构	_	_
9	画	画	v	v	_	8	介宾关系	_	_
10	雄鹰	雄鹰	n	n	_	9	动宾关系	_	_
11	、	、	wp	w	_	12	标点符号	_	_
12	松鼠	松鼠	n	n	_	10	并列关系	_	_
13	和	和	c	cc	_	14	左附加关系	_	_
14	麻雀	麻雀	n	n	_	10	并列关系	_	_
15	作为	作为	p	p	_	6	动宾关系	_	_
16	主攻	主攻	v	vn	_	17	定中关系	_	_
17	目标	目标	n	n	_	15	动宾关系	_	_
18	。	。	wp	w	_	4	标点符号	_	_
```

### 服务器

通过`hanlp serve`来启动内置的http服务器，默认本地访问地址为：http://localhost:8765 ；也可以访问官网演示页面：http://hanlp.hankcs.com/ 。

### 升级

通过`hanlp update`命令来将[HanLP1.x](https://github.com/hankcs/HanLP/tree/1.x)升级到最新版。该命令会获取[HanLP主项目最新版本](https://github.com/hankcs/HanLP/releases)并自动下载安装。

欢迎通过`hanlp --help`查看最新帮助手册。

## API

通过工具类[`HanLP`](https://github.com/hankcs/HanLP/blob/1.x/src/main/java/com/hankcs/hanlp/HanLP.java#L55)调用常用接口：

```python
from pyhanlp import *

print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
for term in HanLP.segment('下雨天地面积水'):
    print('{}\t{}'.format(term.word, term.nature)) # 获取单词与词性
testCases = [
    "商品和服务",
    "结婚的和尚未结婚的确实在干扰分词啊",
    "买水果然后来世博园最后去世博会",
    "中国的首都是北京",
    "欢迎新老师生前来就餐",
    "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
    "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"]
for sentence in testCases: print(HanLP.segment(sentence))
# 关键词提取
document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
           "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
           "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
           "严格地进行水资源论证和取水许可的批准。"
print(HanLP.extractKeyword(document, 2))
# 自动摘要
print(HanLP.extractSummary(document, 3))
# 依存句法分析
print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))
```

### 更多功能

更多功能，包括但不限于：

- 自定义词典
- 极速词典分词
- 索引分词
- CRF分词
- 感知机词法分析
- 臺灣正體、香港繁體
- 关键词提取、自动摘要
- 文本分类、情感分析

请阅读[HanLP主项目文档](https://github.com/hankcs/HanLP/blob/1.x/README.md)和[demos目录](https://github.com/hankcs/pyhanlp/tree/master/tests/demos)以了解更多。调用更底层的API需要参考Java语法用JClass引入更深的类路径。以感知机词法分析器为例，这个类位于包名[`com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer`](https://github.com/hankcs/HanLP/blob/1.x/src/main/java/com/hankcs/hanlp/model/perceptron/PerceptronLexicalAnalyzer.java)下，所以先用`JClass`得到类，然后就可以调用了：

```
PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
analyzer = PerceptronLexicalAnalyzer()
print(analyzer.analyze("上海华安工业（集团）公司董事长谭旭光和秘书胡花蕊来到美国纽约现代艺术博物馆参观"))
```

输出：

```
[上海/ns 华安/nz 工业/n （/w 集团/n ）/w 公司/n]/nt 董事长/n 谭旭光/nr 和/c 秘书/n 胡花蕊/nr 来到/v [美国/ns 纽约/ns 现代/t 艺术/n 博物馆/n]/ns 参观/v
```

如果你需要多线程安全性，可使用`SafeJClass`；如果你需要延迟加载，可使用`LazyLoadingJClass`。如果你经常使用某个类，欢迎将其写入`pyhanlp/__init__.py`中并提交pull request，谢谢！

## 与其他项目共享data

[HanLP1.x](https://github.com/hankcs/HanLP/tree/1.x)具备高度可自定义的特点，所有模型和词典都可以自由替换。如果你希望与别的项目共享同一套data，只需将该项目的配置文件`hanlp.properties`拷贝到pyhanlp的安装目录下即可。本机安装目录可以通过`hanlp --version`获取。

同时，还可以通过`--config`临时加载另一个配置文件：

```
hanlp segment --config path/to/another/hanlp.properties
```

## 测试

```
git clone https://github.com/hankcs/pyhanlp.git
cd pyhanlp
pip install -e .
python tests/test_hanlp.py
```

## 反馈

任何bug，请前往[HanLP issue区](https://github.com/hankcs/HanLP/issues)。提问请上[论坛](https://bbs.hankcs.com/)反馈，谢谢。

## [《自然语言处理入门》](http://nlp.hankcs.com/book.php)

自然语言处理是一门博大精深的学科，掌握理论才能发挥出工具的全部性能。新手可考虑这本入门书：

![img](http://file.hankcs.com/img/nlp-book-squre.jpg)

一本配套HanLP的NLP入门书，基础理论与生产代码并重，Python与Java双实现。从基本概念出发，逐步介绍中文分词、词性标注、命名实体识别、信息抽取、文本聚类、文本分类、句法分析这几个热门问题的算法原理与工程实现。书中通过对多种算法的讲解，比较了它们的优缺点和适用场景，同时详细演示生产级成熟代码，助你真正将自然语言处理应用在生产环境中。

[《自然语言处理入门》](http://nlp.hankcs.com/book.php)由南方科技大学数学系创系主任夏志宏、微软亚洲研究院副院长周明、字节跳动人工智能实验室总监李航、华为诺亚方舟实验室语音语义首席科学家刘群、小米人工智能实验室主任兼NLP首席科学家王斌、中国科学院自动化研究所研究员宗成庆、清华大学副教授刘知远、北京理工大学副教授张华平和52nlp作序推荐。感谢各位前辈老师，希望这个项目和这本书能成为大家工程和学习上的“蝴蝶效应”，帮助大家在NLP之路上蜕变成蝶。

## 授权协议

Apache License 2.0



