#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(len('hello'), 'hello'.__len__())

"""
多行注释
打印版本信息
"""

import sys
print(sys.version)
print(sys.version_info)

def foo():
    pass

def bar():
    pass
  
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
