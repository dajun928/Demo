# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
def del_files(path):
    for root , dirs, files in os.walk(path):
        print root,dirs,files
        for name in files:
            if name.endswith(".jpg"):
                print name
            else:
                print ("Delete File: " + os.path.join(root, name))

if __name__ == "__main__":
    path = u'D:\\Users\\40325\\Pictures\\mv\\新建文件夹\\可乐Vicky 大理旅拍 第一刊 - 微风的日志 - 网易博客_files'
    del_files(path)