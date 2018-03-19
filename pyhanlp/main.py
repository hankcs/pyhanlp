# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-19 01:05
import argparse
import sys

import os
from jpype import JClass

from pyhanlp import HanLP, server
from pyhanlp.static import eprint, PATH_CONFIG, update_hanlp, HANLP_JAR_VERSION, HANLP_JAR_PATH, HANLP_DATA_PATH, \
    hanlp_installed_data_version


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
    args = arg_parser.parse_args()

    def die(msg):
        eprint(msg)
        exit(1)

    if hasattr(args, 'config') and args.config:
        if os.path.isfile(args.config):
            JClass('com.hankcs.hanlp.utility.Predefine').HANLP_PROPERTIES_PATH = args.config
        else:
            die('Can\'t find config file {}'.format(args.config))

    if args.version:
        print('jar  {}: {}'.format(HANLP_JAR_VERSION, HANLP_JAR_PATH))
        data_version = hanlp_installed_data_version()
        print('data {}: {}'.format(data_version if data_version else '自定义', HANLP_DATA_PATH))

    if args.task == 'segment':
        for line in sys.stdin:
            line = line.strip()
            print(' '.join(term.toString() for term in HanLP.segment(line)))
    elif args.task == 'parse':
        for line in sys.stdin:
            line = line.strip()
            print(HanLP.parseDependency(line))
    elif args.task == 'serve':
        server.run(port=args.port)
    elif args.task == 'update':
        update_hanlp()


if __name__ == '__main__':
    main()
