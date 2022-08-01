# !/usr/bin/env python
# encoding: utf-8
# @Time    : 2022.7.30
# @Author  : lqxzd
# @desc    : 批量重命名文件

import os


def replaceFileName(path, replaceStr, newReplaceStr = "", prefix = ""):

    '''
    批量替换文件名，适用于多个文件含同一串字符
    :param path: 文件路径
    :param replaceStr: 待替换的字符
    :param newReplaceStr: 替换后的字符
    :param prefix: 文件名开头（用于准确定位要替换的文件）
    '''

    # 获取目录下的所有文件
    files = os.listdir(path)


    for file in files:
        if file.startswith(prefix):
            # print(file)
            new_file = file.replace(replaceStr, newReplaceStr)
            os.rename(path + '/' + file, path + '/' + new_file)
            print('重命名成功：', file, '-->', new_file)



def splitFileName(path, splitStr, prefix = "", saveIndex = 1):

    '''
    批量分割文件名，适用于多个文件含同一串字符
    :param path: 文件路径
    :param splitStr: 分割字符
    :param prefix: 文件名开头（用于准确定位要分割的文件）
    :param saveIndex: 分割后的索引 (保留分割字符前为0, 保留后为1, 默认为1)
    '''

    # 获取目录下的所有文件
    files = os.listdir(path)


    for file in files:

        newFileName = file.split(splitStr)[saveIndex]
        # print(newFileName)
        if file.startswith(prefix):
            new_file = file.replace(file, newFileName)
            os.rename(path + '/' + file, path + '/' + new_file)
            print('重命名成功：', file, '-->', new_file)


