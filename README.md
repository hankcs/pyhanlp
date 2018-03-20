# pyhanlp: Python interfaces for HanLP

HanLP的Python接口，支持自动下载与升级HanLP，兼容py2、py3。

## 安装

### Python3

```
pip3 install pyhanlp
```

### Python2

```
pip install pyhanlp
```

使用命令`hanlp`来验证安装，如因网络等原因自动安装HanLP失败，可参考[《手动配置》](https://github.com/hankcs/pyhanlp#%E6%89%8B%E5%8A%A8%E9%85%8D%E7%BD%AE)。

## 命令行

### 中文分词

使用命令`hanlp segment`进入交互分词模式，输入一个句子并回车，HanLP会输出分词结果：

```
$ hanlp segment
商品和服务
商品/n 和/cc 服务/vn
当下雨天地面积水分外严重
当/p 下雨天/n 地面/n 积水/n 分外/d 严重/a
龚学平等领导说,邓颖超生前杜绝超生
龚学平/nr 等/udeng 领导/n 说/v ,/w 邓颖超/nr 生前/t 杜绝/v 超生/vi
```

还可以重定向输入输出到文件等：

```
$ hanlp segment <<< '欢迎新老师生前来就餐'               
欢迎/v 新/a 老/a 师生/n 前来/vi 就餐/vi
```

### 依存句法分析

命令为`hanlp parse`，同样支持交互模式和重定向：

```
$ hanlp parse <<< '徐先生还具体帮助他确定了把画雄鹰、松鼠 和麻雀作为主攻目标。'         
1       徐先生  徐先生  nh      nr      _       4       主谓关系        _      _
2       还      还      d       d       _       4       状中结构        _      _
3       具体    具体    a       a       _       4       状中结构        _      _
4       帮助    帮助    v       v       _       0       核心关系        _      _
5       他      他      r       rr      _       4       兼语    _       _
6       确定    确定    v       v       _       4       动宾关系        _      _
7       了      了      u       ule     _       6       右附加关系      _      _
8       把      把      p       pba     _       9       状中结构        _      _
9       画      画      v       v       _       6       动宾关系        _      _
10      雄鹰    雄鹰    n       n       _       9       动宾关系        _      _
11      、      、      wp      w       _       12      标点符号        _      _
12      松鼠    松鼠    n       n       _       10      并列关系        _      _
13                      wp      w       _       9       标点符号        _      _
14      和      和      c       cc      _       15      左附加关系      _      _
15      麻雀    麻雀    n       n       _       16      主谓关系        _      _
16      作为    作为    p       p       _       9       并列关系        _      _
17      主攻    主攻    v       vn      _       18      定中关系        _      _
18      目标    目标    n       n       _       16      动宾关系        _      _
19      。      。      wp      w       _       4       标点符号        _      _
```

### 服务器

通过`hanlp serve`来启动内置的http服务器，默认本地访问地址为：http://localhost:8765 ；也可以访问官网演示页面：http://hanlp.hankcs.com/ 。

### 升级

通过`hanlp update`命令来将HanLP升级到最新版。该命令会获取GitHub最新版本并自动下载安装。

欢迎通过`hanlp --help`查看最新帮助手册。

## API

通过工具类`HanLP`调用常用接口：

```python
from pyhanlp import *

print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
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

请阅读[HanLP主项目文档](https://github.com/hankcs/HanLP)以了解更多。调用更底层的API需要参考Java语法用JClass引入更深的类路径。以感知机词法分析器为例，这个类位于包名[`com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer`](https://github.com/hankcs/HanLP/blob/master/src/main/java/com/hankcs/hanlp/model/perceptron/PerceptronLexicalAnalyzer.java)下，所以先用`JClass`得到类，然后就可以调用了：

```
PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
analyzer = PerceptronLexicalAnalyzer()
print(analyzer.analyze("上海华安工业（集团）公司董事长谭旭光和秘书胡花蕊来到美国纽约现代艺术博物馆参观"))
```

输出：

```
[上海/ns 华安/nz 工业/n （/w 集团/n ）/w 公司/n]/nt 董事长/n 谭旭光/nr 和/c 秘书/n 胡花蕊/nr 来到/v [美国/ns 纽约/ns 现代/t 艺术/n 博物馆/n]/ns 参观/v
```

如果你经常使用某个类，欢迎将其写入`pyhanlp/__init__.py`中并提交pull request，谢谢！

## 与其他项目共享data

HanLP具备高度可自定义的特点，所有模型和词典都可以自由替换。如果你希望与别的项目共享同一套data，只需将该项目的配置文件`hanlp.properties`拷贝到pyhanlp的安装目录下即可。本机安装目录可以通过`hanlp --version`获取。

同时，还可以通过`--config`临时加载另一个配置文件：

```
hanlp segment --config path/to/another/hanlp.properties
```

## 配置

### 自动配置

默认在首次调用HanLP时自动下载jar包和数据包，并自动完成配置。

### 手动配置

如因网络等原因自动配置失败，可以通过设置环境变量来自定义HanLP版本和数据位置。

| 变量名 | 默认值 | 备注 |
| --- | --- | --- |
| HANLP\_STATIC\_ROOT | pyhanlp所在安装路径的static文件夹 | 配置文件hanlp.properties所在的目录| 
| HANLP_JAR_PATH | pyhanlp所在安装路径的static文件夹 | HanLP jar 包位置 | 


注意：

1. **使用pip初次安装 pyhanlp 后，不设置上述变量，程序会自动下载所需依赖到默认位置。如果是设置了上述变量，则不进行下载。因为文件比较大，网络下载稳定性等原因，建议提前准备好[jar](https://mvnrepository.com/artifact/com.hankcs/hanlp)包，[配置文件](https://github.com/hankcs/HanLP#3%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)和[data](https://github.com/hankcs/HanLP#2%E4%B8%8B%E8%BD%BDdata)，并使用环境变量进行配置。**

2. 保证 hanlp.properties 中的 root 是指向正确的data路径。

比如：

```
export HANLP_JAR_PATH=/hanlp/hanlp-portable-1.6.0.jar
export HANLP_STATIC_ROOT=/hanlp
```

就需要保证有如下的目录结构：

```
hanlp
├── data
│   ├── README.url
│   ├── dictionary
│   └── model
├── hanlp.properties
└── hanlp-portable-1.6.0.jar
```

## 测试

```
git clone https://github.com/hankcs/pyhanlp.git
cd pyhanlp
pip install -r requirements.txt # 安装依赖
export HANLP_JAR_PATH=          # 配置环境变量
export HANLP_STATIC_ROOT=       # 配置环境变量
python tests/test_hanlp.py      # 执行测试
```


## 授权协议

Apache License 2.0



