# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-19 01:05
from __future__ import print_function
from __future__ import division

import os
import sys

from pyhanlp.util import any2utf8

PY = 3
if sys.version_info[0] < 3:
    PY = 2
    # noinspection PyUnresolvedReferences
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import argparse
from jpype import JClass

from pyhanlp import HanLP
from pyhanlp.static import eprint, PATH_CONFIG, update_hanlp, HANLP_JAR_VERSION, HANLP_JAR_PATH, HANLP_DATA_PATH, \
    hanlp_installed_data_version, STATIC_ROOT


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')

    arg_parser = argparse.ArgumentParser(description='HanLP: Han Language Processing v{}'.format(HANLP_JAR_VERSION))
    arg_parser.add_argument('-v', '--version', required=False, action='store_true',
                            help='show installed versions of HanLP')
    task_parser = arg_parser.add_subparsers(dest="task", help='which task to perform?')
    segment_parser = task_parser.add_parser(name='segment', help='word segmentation')
    parse_parser = task_parser.add_parser(name='parse', help='dependency parsing')
    server_parser = task_parser.add_parser(name='serve', help='start http server', description='A http server for HanLP')
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

    def die(msg):
        eprint(msg)
        exit(1)

    if hasattr(args, 'config') and args.config:
        if os.path.isfile(args.config):
            JClass('com.hankcs.hanlp.utility.Predefine').HANLP_PROPERTIES_PATH = args.config
        else:
            die('Can\'t find config file {}'.format(args.config))

    if args.task == 'segment':
        for line in sys.stdin:
            line = line.strip()
            print(' '.join(term.toString() for term in HanLP.segment(any2utf8(line))))
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
        update_hanlp()


if __name__ == '__main__':
    main()
