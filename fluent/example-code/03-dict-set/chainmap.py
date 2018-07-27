# _*_ coding: utf-8 _*_
import collections
import os
import argparse

__author__ = 'david'
__date__ = '2018/7/27 22:18'


def chainmap_demo():
    defaults = {'color': 'red', 'user': 'guest'}
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = {k: v for k, v in vars(namespace).items() if v}
    combined = collections.ChainMap(command_line_args, os.environ, defaults)
    print(combined['color'])
    print(combined['user'])


if __name__ == '__main__':
    chainmap_demo()
