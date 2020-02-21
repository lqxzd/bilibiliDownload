#!/usr/bin/env python
# encoding: utf-8

import os
import json
import requests




def getResultUrl(url):
    # url = "https://www.bilibili.com/video/av84357959"
    headers = {'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; U8860 Build/HuaweiU8860) UC AppleWebKit/530+ (KHTML, like Gecko) Mobile Safari/530'}
    res = requests.get(url, headers=headers)

    res_text = res.text
    dlURL = res_text.split('"initUrl":"//')[1].split('"')[0]
    resultUrl = "https://"+dlURL
    return resultUrl



url = input("url：")
print(getResultUrl(url))
