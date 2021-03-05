# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-18 20:05
from __future__ import division
from __future__ import print_function

import os
import platform
import shutil
import ssl
import sys

from hanlp_downloader import Downloader
from hanlp_downloader.log import DownloadCallback

from pyhanlp.util import eprint, browser_open

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, os.path.pardir))
ssl._create_default_https_context = ssl._create_unverified_context

PY = 3
if sys.version_info[0] < 3:
    PY = 2
    # noinspection PyUnresolvedReferences
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import errno
import glob
import json
import zipfile
from shutil import copyfile

if PY == 3:
    from urllib.parse import quote
    import urllib.request as urllib


    def open_(*args, **kwargs):
        return open(*args, **kwargs)
else:
    import urllib


    def open_(*args, **kwargs):
        import codecs
        return codecs.open(*args, **kwargs)

import time

STATIC_ROOT = os.path.dirname(os.path.realpath(__file__))
PATH_CONFIG = os.path.join(STATIC_ROOT, 'hanlp.properties')
HANLP_DATA_PATH = os.path.join(STATIC_ROOT, 'data')
PATH_DATA_VERSION = os.path.join(HANLP_DATA_PATH, 'version.txt')
HANLP_JAR_VERSION = None
HANLP_DATA_VERSION = None
HANLP_RELEASES = None
INDEX_HTML = os.path.join(STATIC_ROOT, 'index.html')


def remove_file(filename):
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred


def hanlp_latest_version():
    return hanlp_releases()[0]


def hanlp_releases(cache=True):
    global HANLP_RELEASES
    if cache and HANLP_RELEASES:
        return HANLP_RELEASES
    # print('Request GitHub API')
    req = urllib.Request('http://nlp.hankcs.com/download.php?file=version')
    req.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36')
    if PY == 3:
        content = urllib.urlopen(req).read()
    else:
        content = urllib.urlopen(req).read()
    content = json.loads(content.decode())
    jar_version, jar_url, data_version, data_url = content
    meta = [(jar_version, jar_url, data_version, data_url)]
    HANLP_RELEASES = meta
    return meta


def hanlp_installed_jar_versions():
    # print(glob.glob(os.path.join(STATIC_ROOT, 'hanlp-{}.jar'.format(version))))
    # if not version:
    #     pass
    # if os.path.exists(version):
    #     pass
    versions = []
    for jar in glob.glob(os.path.join(STATIC_ROOT, 'hanlp-*.jar')):
        versions.append(os.path.basename(jar)[len('hanlp-'):-len('.jar')])

    versions = sorted(versions, reverse=True)
    if versions:
        global HANLP_JAR_VERSION
        HANLP_JAR_VERSION = versions[0]
    return versions


def hanlp_installed_data_version():
    try:
        with open_(os.path.join(HANLP_DATA_PATH, 'version.txt'), encoding='utf-8') as f:
            global HANLP_DATA_VERSION
            HANLP_DATA_VERSION = f.readlines()[0].strip()
            return HANLP_DATA_VERSION
    except:
        return None


def hanlp_installed_data_path():
    root = read_config()
    if os.path.isdir(root):
        global HANLP_DATA_PATH
        if root == STATIC_ROOT:
            if not os.path.isdir(HANLP_DATA_PATH):
                return None
        HANLP_DATA_PATH = os.path.join(root, 'data')
        return HANLP_DATA_PATH

    return None


def download(url, path):
    opener = urllib.build_opener()
    opener.addheaders = [('User-agent',
                          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36')]
    urllib.install_opener(opener)
    if os.path.isfile(path):
        print('使用本地 {}, 忽略 {}'.format(path, url))
        return True
    else:
        print('下载 {} 到 {}'.format(url, path))
        tmp_path = '{}.downloading'.format(path)
        remove_file(tmp_path)
        try:
            downloader = Downloader(url, tmp_path, 4, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'})
            downloader.subscribe(DownloadCallback(show_header=False, out=sys.stdout))
            downloader.start_sync()
        except BaseException as e:
            eprint('下载失败 {} 由于 {}'.format(url, repr(e)))
            doc_url = 'https://od.hankcs.com/book/intro_nlp/'
            eprint('请参考 %s 执行手动安装.' % doc_url)
            eprint('或手动下载 {} 到 {}'.format(url, path))
            if os.path.isfile(tmp_path):
                os.remove(tmp_path)
            browser_open(doc_url)
            exit(1)
        remove_file(path)
        os.rename(tmp_path, path)
    return True


def install_hanlp_jar():
    jar_version, jar_url, data_version, data_url = hanlp_latest_version()
    jar_zip = os.path.join(STATIC_ROOT, 'hanlp-{}-release.zip'.format(jar_version))
    download(jar_url, jar_zip)
    with zipfile.ZipFile(jar_zip, "r") as archive:
        # for f in archive.namelist():
        #     print(f)
        archive.extract('hanlp-{}-release/hanlp-{}.jar'.format(jar_version, jar_version), STATIC_ROOT)
    zip_folder = os.path.join(STATIC_ROOT, 'hanlp-{}-release'.format(jar_version))
    jar_file_name = 'hanlp-{}.jar'.format(jar_version)
    os.rename(os.path.join(zip_folder, jar_file_name), os.path.join(STATIC_ROOT, jar_file_name))
    shutil.rmtree(zip_folder)
    remove_file(jar_zip)
    global HANLP_JAR_VERSION
    HANLP_JAR_VERSION = jar_version


def update_hanlp():
    if update_hanlp_jar():
        print('HanLP jar 已被升级到最新版本 {}'.format(HANLP_JAR_VERSION))
    else:
        print('HanLP jar 已经是最新版本 {}'.format(HANLP_JAR_VERSION))

    root = read_config()
    if root == STATIC_ROOT:
        if install_hanlp_data(HANLP_JAR_VERSION):
            print('HanLP data 已被升级到最新版本 {}'.format(HANLP_DATA_VERSION))
        else:
            print('HanLP data 已经是最新版本 {}'.format(HANLP_DATA_VERSION))


def update_hanlp_jar():
    if hanlp_releases()[0][0] in hanlp_installed_jar_versions():
        return False
    install_hanlp_jar()
    uninstall_hanlp_jar()
    return True


def install_hanlp_data(the_jar_version=None):
    if not the_jar_version:
        the_jar_version = HANLP_JAR_VERSION if HANLP_JAR_VERSION else hanlp_latest_version()[0]
    for jar_version, jar_url, data_version, data_url in hanlp_releases():
        if jar_version == the_jar_version:
            if data_version == hanlp_installed_data_version():
                return False
            data_zip = 'data-for-{}.zip'.format(data_version)
            data_zip = os.path.join(STATIC_ROOT, data_zip)
            download(data_url, os.path.join(STATIC_ROOT, data_zip))
            print('解压 data.zip...')
            with zipfile.ZipFile(data_zip, "r") as zip_ref:
                zip_ref.extractall(STATIC_ROOT)
            os.remove(data_zip)
            write_config(root=STATIC_ROOT)
            with open_(PATH_DATA_VERSION, 'w', encoding='utf-8') as f:
                f.write(data_version)
            global HANLP_DATA_VERSION
            HANLP_DATA_VERSION = data_version
            return True


def write_config(root=None):
    if root and os.name == 'nt':
        root = root.replace('\\', '/')  # For Windows
    if root and platform.system().startswith('CYGWIN'):  # For cygwin
        if root.startswith('/usr/lib'):
            cygwin_root = os.popen('cygpath -w /').read().strip().replace('\\', '/')
            root = cygwin_root + root[len('/usr'):]
        elif STATIC_ROOT.startswith('/cygdrive'):
            driver = STATIC_ROOT.split('/')
            cygwin_driver = '/'.join(driver[:3])
            win_driver = driver[2].upper() + ':'
            root = root.replace(cygwin_driver, win_driver)
    content = []
    with open_(PATH_CONFIG, encoding='utf-8') as f:
        for line in f:
            if root:
                if line.startswith('root'):
                    line = 'root={}{}'.format(root, os.linesep)
            content.append(line)
    with open_(PATH_CONFIG, 'w', encoding='utf-8') as f:
        f.writelines(content)


def read_config():
    root = None
    if not os.path.isfile(PATH_CONFIG):
        copyfile(PATH_CONFIG + '.in', PATH_CONFIG)
        write_config(root=STATIC_ROOT)
    with open_(PATH_CONFIG, encoding='utf-8') as f:
        for line in f:
            if line.startswith('root'):
                root = line.strip().split('=')[1]
    return os.path.abspath(root)


def hanlp_jar_path(version):
    return os.path.join(STATIC_ROOT, 'hanlp-{}.jar'.format(version))


def uninstall_hanlp_jar(version='old'):
    if version == 'old':
        vs = hanlp_installed_jar_versions()
        if len(vs) > 1:
            if vs[0].startswith('portable'):
                remove_file(hanlp_jar_path(vs[0]))
                vs = vs[1:]
                global HANLP_JAR_VERSION
                HANLP_JAR_VERSION = vs[0]
            for v in vs[1:]:
                remove_file(hanlp_jar_path(v))
    else:
        remove_file(hanlp_jar_path(version))


if not hanlp_installed_jar_versions():
    install_hanlp_jar()

if not hanlp_installed_data_path():
    install_hanlp_data(HANLP_JAR_VERSION)

HANLP_JAR_PATH = hanlp_jar_path(HANLP_JAR_VERSION)

# install_hanlp_jar('1.5.4')
# print(hanlp_releases())
# print(hanlp_installed('1.6.0'))
# print(hanlp_installed_jar_versions())
# uninstall_hanlp_jar()
# update_hanlp_jar()
# print(_HANLP_JAR_PATH)
# write_config(data_version='1.6.0')
# print(hanlp_installed_data_versions())
# download('http://storage.live.com/items/D4A741A579C555F7!65703:/data-for-1.6.0.zip', 'tmp')
# print(hanlp_installed_data_version())
