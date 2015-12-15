#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'deangao'
__version__ = '1.0.0'

from pytextscan import core

def textScan():
    '''对敏感信息进行识别及过滤 '''
    
    scaner = core.Scanner(u'12232 ')
    print scaner.doScan()
    
def main():
    textScan()
    
if __name__ == '__main__':
    main()