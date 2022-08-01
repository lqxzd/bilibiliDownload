#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022.7.31
# @Author  : lqxzd
# @desc    : 批量合并音频和视频

import os

def merge(inputPath, outputPath, ffmpegPath):

    '''
    :param inputPath: 视频和音频源地址
    :param outputPath: 视频输出地址
    :param ffmpegPath: ffmpeg环境地址 (bin目录下)
    '''

    # 获取目录下的所有文件
    files = os.listdir(inputPath)

    videoList = []
    audioList = []


    for i in range(len(files)):
        if(i % 2 == 0):
            videoList.append(files[i])
        else:
            audioList.append(files[i])

    for i in range(len(videoList)):

        outName = outputPath + "\\" + str(videoList[i]).split("[")[0] + ".mp4"
        video = inputPath + "\\" + videoList[i]
        audio = inputPath + "\\" + audioList[i]

        # ffmpeg -i "audio.mp4" -i "video.mp4" -b:v 1000k -c:v hevc_nvenc output.mp4
        cmand = ffmpegPath + "\\" + "ffmpeg -i " + '"' + video + '"' + " -i " + '"' + audio + '"' + " -b:v 1000k -c:v hevc_nvenc " + '"' + outName + '"'

        # print(cmand)
        os.system(cmand)


