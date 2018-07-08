#encoding=utf-8
from MysqlHelper import MysqlHelper


sname=["a","b","c","d"]

sql="insert into stu(name) values(%s)"

for name in sname:
    param = [name]

    sqlhelper.insert(sql, param)

