# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-19 01:05
from __future__ import division
from __future__ import print_function

import os
import sys
import argparse
from jpype import JClass, JException, java
# noinspection PyUnresolvedReferences
from pyhanlp import HanLP, PATH_CONFIG, HANLP_JAR_VERSION, HANLP_JAR_PATH, HANLP_DATA_PATH, \
    hanlp_installed_data_version, STATIC_ROOT
from pyhanlp.util import any2utf8

PY = 3
if sys.version_info[0] < 3:
    PY = 2
    # noinspection PyUnresolvedReferences,PyCompatibility
    reload(sys), sys.setdefaultencoding("utf-8")


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')

    arg_parser = argparse.ArgumentParser(description='HanLP: Han Language Processing v{}'.format(HANLP_JAR_VERSION))
    arg_parser.add_argument('-v', '--version', required=False, action='store_true',
                            help='show installed versions of HanLP')
    task_parser = arg_parser.add_subparsers(dest="task", help='which task to perform?')
    segment_parser = task_parser.add_parser(name='segment', help='word segmentation')
    tag_parser = segment_parser.add_mutually_exclusive_group(required=False)
    tag_parser.add_argument('--tag', dest='tag', action='store_true', help='show part-of-speech tags')
    tag_parser.add_argument('--no-tag', dest='tag', action='store_false', help='don\'t show part-of-speech tags')
    segment_parser.set_defaults(tag=True)
    segment_parser.add_argument('-a', '--algorithm', type=str, default='viterbi',
                                help='algorithm of segmentation e.g. perceptron')
    parse_parser = task_parser.add_parser(name='parse', help='dependency parsing')
    server_parser = task_parser.add_parser(name='serve', help='start http server',
                                           description='A http server for HanLP')
    server_parser.add_argument('--port', type=int, default=8765)
    update_parser = task_parser.add_parser(name='update', help='update jar and data of HanLP')

    def add_args(p):
        p.add_argument("--config", default=PATH_CONFIG,
                       help='path to hanlp.properties')
        # p.add_argument("--action", dest="action", default='predict',
        #                help='Which action (train, test, predict)?')

    add_args(segment_parser)
    add_args(parse_parser)

    if '-v' in sys.argv or '--version' in sys.argv:
        print('jar  {}: {}'.format(HANLP_JAR_VERSION, HANLP_JAR_PATH))
        data_version = hanlp_installed_data_version()
        print('data {}: {}'.format(data_version if data_version else '自定义', HANLP_DATA_PATH))
        print('config    : {}'.format(os.path.join(STATIC_ROOT, 'hanlp.properties')))
        exit(0)

    args = arg_parser.parse_args()

    def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)

    def die(msg):
        eprint(msg)
        exit(1)

    if hasattr(args, 'config') and args.config:
        if os.path.isfile(args.config):
            JClass('com.hankcs.hanlp.utility.Predefine').HANLP_PROPERTIES_PATH = args.config
        else:
            die('Can\'t find config file {}'.format(args.config))

    if args.task == 'segment':
        segmenter = None
        try:
            segmenter = HanLP.newSegment(args.algorithm)
        except JException as e:
            if isinstance(e, java.lang.IllegalArgumentException):
                die('invalid algorithm {}'.format(args.algorithm))
            elif isinstance(e, java.lang.RuntimeException):
                die('failed to load required model')
            else:
                die('unknown exception {}'.format(repr(e)))

        is_lexical_analyzer = hasattr(segmenter, 'analyze')
        if not args.tag:
            if is_lexical_analyzer:
                segmenter.enablePartOfSpeechTagging(False)
                JClass('com.hankcs.hanlp.HanLP$Config').ShowTermNature = False
            else:
                JClass('com.hankcs.hanlp.HanLP$Config').ShowTermNature = False
        for line in sys.stdin:
            line = line.strip()
            print(' '.join(term.toString() for term in segmenter.seg(any2utf8(line))))
    elif args.task == 'parse':
        for line in sys.stdin:
            line = line.strip()
            print(HanLP.parseDependency(any2utf8(line)))
    elif args.task == 'serve':
        if PY == 3:
            from pyhanlp import server
            server.run(port=args.port)
        else:
            die('现在server.py暂时不支持Python2，欢迎参与移植')
    elif args.task == 'update':
        if hanlp_installed_data_version() == '手动安装':
            die('手动配置不支持自动升级，若要恢复自动安装，请清除HANLP相关环境变量')
        else:
            from pyhanlp.static import update_hanlp
            update_hanlp()


if __name__ == '__main__':
    main()
