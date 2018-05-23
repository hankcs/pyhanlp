# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-23 17:35
import zipfile
import os

from pyhanlp.static import download, remove_file


def test_data_path():
    this_dir = os.getcwd()
    # print(this_dir)
    data_path = os.path.join(this_dir, 'data')
    if os.path.isdir(data_path):
        return data_path
    data_path = os.path.join(this_dir[:this_dir.find('pyhanlp')], 'pyhanlp', 'tests', 'data')
    if os.path.isdir(data_path):
        return data_path
    raise FileNotFoundError('找不到测试data目录，请在项目根目录下运行测试脚本')


def ensure_data(data_name, data_url):
    root_path = test_data_path()
    dest_path = os.path.join(root_path, data_name)
    if os.path.exists(dest_path):
        return dest_path
    if data_url.endswith('.zip'):
        dest_path += '.zip'
    download(data_url, dest_path)
    if data_url.endswith('.zip'):
        with zipfile.ZipFile(dest_path, "r") as archive:
            archive.extractall(root_path)
        remove_file(dest_path)
        dest_path = dest_path[:-len('.zip')]
    return dest_path
