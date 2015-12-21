#!/usr/bin/python
# -*- coding: utf8 -*-

__author__ = 'deangao'
__version__ = '1.0.0'

from pytextscan import core
import logging.config

def textScan():
    '''对敏感信息进行识别及过滤 '''
    
    logging.config.fileConfig("../conf/logger.conf")
    logger = logging.getLogger("pytextscan")
    
    data = '高文辉的手机号是15002712111ok?'
    logger.info(data)
    scaner = core.Scanner(data)
    print scaner.doScan()
    
    masker = core.Masker(data)
    logger.info(data)
    print masker.doMask()
    
def main():
    textScan()
    
if __name__ == '__main__':
    main()
    