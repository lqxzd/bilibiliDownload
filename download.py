#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020.10.06
# @Author  : lqxzd
# @desc    : you-get批量下载 B站视频

import os
import sys
import you_get

def download(url, path, length):

    '''
    :param url: 视频链接
    :param path: 视频保存地址
    :param length: 视频个数
    '''

    # 定位到当前脚本所在的路径
    # root = os.path.dirname(os.path.realpath(__file__))

    for i in range(0,length):
        video_url = url + "?p=" + str(i)
        try:
            sys.argv = ['you-get','--format=dash-flv','-o',path,video_url]
            you_get.main()
        except:
            sys.argv = ['you-get','--format=dash-flv720','-o',path,video_url]
            you_get.main()
