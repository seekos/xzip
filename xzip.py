#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import zipfile
reload(sys)
sys.setdefaultencoding('utf8');

#将多个相邻的符号替换成一个
def su_str_replace(str0,flag = '_'):
    str1 = str0.replace(flag+flag,flag);
    if str1 == str0:
        return str1;
    else:
        return su_str_replace(str1,flag)

#f = file('/tmp/zip.err', 'w')
#sys.stderr = f

if len(sys.argv) < 3:  
   print("缺少参数");
   sys.exit();

file = zipfile.ZipFile(sys.argv[1],"r");
saveto = os.path.abspath(sys.argv[2]);

#print(saveto);
#sys.exit();

if not os.path.exists(saveto):
   os.makedirs(saveto);

file=zipfile.ZipFile(sys.argv[1],"r");
#print(file.namelist());
for name in file.namelist():
    #print(type(name).__name__);
    if type(name).__name__ != "unicode":
        utf8name=name.decode('gbk', 'ignore');
    else:
        utf8name = name;

    #print(utf8name);
    #替换特殊字符,需要保留的添加,其他的字符替换为下滑线
    flag = '_';
    #p = u"[^0-9A-Za-z\u4e00-\u9fa5\.\_\/\-]";
    p = u"[^0-9A-Za-z\u4e00-\u9fa5\.\_\/]";
    utf8name = re.sub(p, flag, utf8name);

    utf8name = su_str_replace(utf8name,flag);

    pathname = saveto + '/' + os.path.dirname(utf8name);

    if not os.path.exists(pathname):
        os.makedirs(pathname);
        print("创建目录 " + pathname);
    else:
        data = file.read(name);
        if not os.path.exists(saveto + '/' + utf8name) and len(data) > 0:
            print("创建文件 " + utf8name);
            fo = open(saveto + '/' + utf8name, "w");
            fo.write(data);
            fo.close;
file.close()
