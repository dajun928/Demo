# -*- coding:utf-8 -*-

#有问题 待解决
import urllib.request

url= "http://www.baidu.com"
data = urllib.request.urlopen(url).read()#
data = data.decode('UTF-8')
print(data)















