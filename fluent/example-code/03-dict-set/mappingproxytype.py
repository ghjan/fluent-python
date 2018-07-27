# _*_ coding: utf-8 _*_
__author__ = 'david'
__date__ = '2018/7/27 22:57'

from types import MappingProxyType


def mappingproxytype_demo():
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)
    try:
        d_proxy[1] = 'B'  # TypeError: 'mappingproxy' object does not support item assignment
    except TypeError:
        pass
    d[2] = 'B'  # 不能修改已有的键值对，但是可以添加新的键值对
    print(d_proxy)  # mappingproxy({1: 'A', 2: 'B'})


if __name__ == '__main__':
    mappingproxytype_demo()
