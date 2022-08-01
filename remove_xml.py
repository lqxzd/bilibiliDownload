# !/usr/bin/env python
# encoding: utf-8
# @Time    : 2020.10.06
# @Author  : lqxzd
# @desc    : 一键删除xml文件

from gettext import find
import os
import sys
import glob


def remove_xml(path):

     print("删除文件：")
     print("-------------------")

     try:
          xmlFile = glob.glob(os.path.join(path, '*.cmt.xml'))
          # print(xmlFile)
          for infile in xmlFile:
               os.remove(infile)
               print(infile)    
     except:
          print("Unexpected error:", sys.exc_info()[0])
          raise

     print("删除成功")
