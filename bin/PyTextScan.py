#!/usr/bin/python
# -*- coding: utf8 -*-

__author__ = 'deangao'
__version__ = '1.0.0'

import logging.config

def textScan():
    '''对敏感信息进行识别及过滤 '''
    
    logging.config.fileConfig("../conf/logger.conf")
    logger = logging.getLogger("pytextscan")
    
def main():
    textScan()
    
if __name__ == '__main__':
    main()
    