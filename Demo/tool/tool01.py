# -*- coding: utf-8 -*-
"""
Created on Sun Sep 03 22:01:25 2017
@author: Administrator
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".jpg"):
                # os.remove(os.path.join(root,name))
                print name
            else:
                os.remove(os.path.join(root,name))
                print ("Delete File: " + os.path.join(root, name))

# test
if __name__ == "__main__":
    path = u'D:\\Users\\40325\\Pictures\\mv\\新建文件夹\\可乐Vicky 大理旅拍 第一刊 - 微风的日志 - 网易博客_files'
    del_files(path)