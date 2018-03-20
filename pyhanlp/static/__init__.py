# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-18 20:05
from __future__ import division
from __future__ import print_function

import os
import sys

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, os.path.pardir))

PY = 3
if sys.version_info[0] < 3:
    PY = 2
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import errno
import glob
import json
import re
import zipfile
from shutil import copyfile
if PY == 3:
    import urllib.request as urllib
else:
    import urllib

import time

STATIC_ROOT = os.path.dirname(os.path.realpath(__file__))
PATH_CONFIG = os.path.join(STATIC_ROOT, 'hanlp.properties')
HANLP_DATA_PATH = os.path.join(STATIC_ROOT, 'data')
PATH_DATA_VERSION = os.path.join(HANLP_DATA_PATH, 'version.txt')
HANLP_JAR_VERSION = None
HANLP_DATA_VERSION = None
HANLP_RELEASES = None
INDEX_HTML = os.path.join(STATIC_ROOT, 'index.html')


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


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
    content = urllib.urlopen("https://api.github.com/repos/hankcs/HanLP/releases").read()
    # https://stackoverflow.com/questions/48174702/python-unable-to-load-a-json-file-with-utf-8-encoding
    content = json.loads(content.decode('utf-8-sig'))
    meta = []
    for r in content:
        jar_version = r['tag_name']
        if jar_version.startswith('v'):
            jar_version = jar_version[1:]
        m = re.search(r'\[(data-for-.*?\.zip)\]\((.*?)\)', r['body'])
        data_version, data_url = None, None
        if m and len(m.groups()) == 2:
            data_version = m.group(1)[len('data-for-'):-len('.zip')]
            data_url = m.group(2)
        meta.append((jar_version, data_version, data_url))

    HANLP_RELEASES = meta
    return meta


def hanlp_installed_jar_versions():
    # print(glob.glob(os.path.join(STATIC_ROOT, 'hanlp-portable-{}.jar'.format(version))))
    # if not version:
    #     pass
    # if os.path.exists(version):
    #     pass
    versions = []
    for jar in glob.glob(os.path.join(STATIC_ROOT, 'hanlp-portable-*.jar')):
        versions.append(os.path.basename(jar)[len('hanlp-portable-'):-len('.jar')])

    versions = sorted(versions, reverse=True)
    if versions:
        global HANLP_JAR_VERSION
        HANLP_JAR_VERSION = versions[0]
    return versions


def hanlp_installed_data_version():
    try:
        with open(os.path.join(HANLP_DATA_PATH, 'version.txt')) as f:
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
    # opener = urllib.build_opener()
    # opener.addheaders = [('User-agent',
    #                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36')]
    # urllib.install_opener(opener)
    print('Downloading {} to {}'.format(url, path))
    tmp_path = '{}.downloading'.format(path)
    try:
        def reporthook(count, block_size, total_size):
            global start_time
            if count == 0:
                start_time = time.time()
                return
            duration = time.time() - start_time
            progress_size = int(count * block_size)
            speed = int(progress_size / (1024 * duration))
            ratio = count * block_size / total_size
            percent = ratio * 100
            eta = duration / ratio * (1 - ratio)
            minutes = eta / 60
            seconds = eta % 60
            sys.stdout.write("\r%.2f%%, %d MB, %d KB/s, ETA %d min %d s" %
                             (percent, progress_size / (1024 * 1024), speed, minutes, seconds))
            sys.stdout.flush()

        urllib.urlretrieve(url, tmp_path, reporthook)
        print()
    except:
        try:
            os.system('wget {} -O {}'.format(url, path))
        except:
            eprint('Failed to download {}'.format(url))
            return False
    os.rename(tmp_path, path)
    return True


def install_hanlp_jar(version=None):
    if version is None:
        version = hanlp_latest_version()[0]
    url = 'http://search.maven.org/remotecontent?filepath=com/hankcs/hanlp/portable-{}/hanlp-portable-{}.jar'.format(
        version, version)
    download(url, hanlp_jar_path(version))
    global HANLP_JAR_VERSION
    HANLP_JAR_VERSION = version


def update_hanlp():
    if update_hanlp_jar():
        print('HanLP jar has been updated to the latest version {}'.format(HANLP_JAR_VERSION))
    else:
        print('HanLP jar is already the latest version {}'.format(HANLP_JAR_VERSION))

    root = read_config()
    if root == STATIC_ROOT:
        if install_hanlp_data(HANLP_JAR_VERSION):
            print('HanLP data has been updated to the latest version {}'.format(HANLP_DATA_VERSION))
        else:
            print('HanLP data is already the latest version {}'.format(HANLP_DATA_VERSION))


def update_hanlp_jar():
    if hanlp_releases()[0][0] in hanlp_installed_jar_versions():
        return False
    install_hanlp_jar()
    uninstall_hanlp_jar()
    return True


def install_hanlp_data(the_jar_version):
    for jar_version, data_version, data_url in hanlp_releases():
        if jar_version == the_jar_version:
            if data_version == hanlp_installed_data_version():
                return False
            data_zip = 'data-for-{}.zip'.format(data_version)
            data_zip = os.path.join(STATIC_ROOT, data_zip)
            download(data_url, os.path.join(STATIC_ROOT, data_zip))
            with zipfile.ZipFile(data_zip, "r") as zip_ref:
                zip_ref.extractall(STATIC_ROOT)
            os.remove(data_zip)
            write_config(root=STATIC_ROOT)
            with open(PATH_DATA_VERSION, 'w') as f:
                f.write(data_version)
            return True


def write_config(root=None):
    content = []
    with open(PATH_CONFIG) as f:
        for line in f:
            if root:
                if line.startswith('root'):
                    line = 'root={}{}'.format(root, os.linesep)
            content.append(line)
    with open(PATH_CONFIG, 'w') as f:
        f.writelines(content)


def read_config():
    root = None
    if not os.path.isfile(PATH_CONFIG):
        copyfile(PATH_CONFIG + '.in', PATH_CONFIG)
    with open(PATH_CONFIG) as f:
        for line in f:
            if line.startswith('root'):
                root = line.strip().split('=')[1]
    return root


def hanlp_jar_path(version):
    return os.path.join(STATIC_ROOT, 'hanlp-portable-{}.jar'.format(version))


def uninstall_hanlp_jar(version='old'):
    if version == 'old':
        vs = hanlp_installed_jar_versions()
        if len(vs) > 1:
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
# update_hanlp()
