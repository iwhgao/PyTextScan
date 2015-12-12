#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'deangao'
__version__ = '1.0.0'

import re
import os
import sys
import logging
import configobj
import argparse

import jieba.posseg as pseg

def scanCNName(s):
    '''中文分词检测中文姓名并处理'''

    jiebaRes = pseg.cut(s)
    for tmp in jiebaRes:
        m = re.findall('(.*?)\/nr', str(tmp))
        if m is not None and len(m) > 0:
            firstName = m[0].decode('utf8')[0:1].encode('utf8')
            s = re.sub(m[0], firstName + '**', s)
    return s

def scanBankCardNo(s):
    '''识别银行卡号并处理'''

    m = re.findall('\D(6\d{14,18})\D', s)
    if m is not None and len(m) > 0:
        for one in m:
            startNum = one[0:6]
            endNum = one[-4:]
            s = re.sub(one, '%s*********%s' % (startNum, endNum), s)
    return s

def scanIdenNo(s):
    '''识别身份证号并处理'''

    m = \
        re.findall('\D([123456789]\d{5}((19)|(20))\d{2}((0[123456789])|(1[012]))((0[123456789])|([12][0-9])|(3[01]))\d{3}[Xx0-9])\D'
                   , s)
    if m is not None and len(m) > 0:
        for one in m:
            if len(one[0]) < 18:
                continue
            startNum = one[0][0]
            endNum = one[0][-1]
            s = re.sub(one[0], '%s***************%s' % (startNum,
                       endNum), s)
    return s

def scanPhoneNo(s):
    '''识别手机开户并处理'''

    m = re.findall('\D(1[3578]\d{9})\D', s)
    if m is not None and len(m) > 0:
        for one in m:
            startNum = one[0:3]
            endNum = one[-2:]
            s = re.sub(one, '%s******%s' % (startNum, endNum), s)
    return s

def scanEmailAddr(s):
    '''识别邮箱地址并处理'''

    m = \
        re.findall('(([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+(\.[a-zA-Z]{2,3})+)'
                   , s)
    if m is not None and len(m) > 0:
        for one in m:
            m1 = re.findall('(\w+)@', one[0])
            maskedOne = re.sub(m1[0], '%s******' % m1[0][0], one[0])
            s = re.sub(one[0], maskedOne, s)
    return s

def textScan(s):
    '''对敏感信息进行识别及过滤 '''

    s = scanBankCardNo(s)
    s = scanIdenNo(s)
    s = scanPhoneNo(s)
    s = scanEmailAddr(s)
    s = scanCNName(s)
    return s


def main():
    
    #load config file
    conf_ini = "../conf/PyTextScan.ini"
    config = configobj.ConfigObj(conf_ini,encoding='UTF8')
    
    #generate the argparse object
    parser = argparse.ArgumentParser(description='''This is a program to scan the text format content 
            by http or socket method with configure file''')

    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')

    print config['server']['servername']
    
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] %(name)s:%(levelname)s: %(message)s'
                        )
    '''
    if not os.path.exists(filename):
        logging.error('Not such file!')
        exit()

   
    f = open(filename, 'r')
    maskedText = ''
    for oneline in f:
        maskedText = maskedText + textScan(oneline)
    print maskedText
    '''
    
if __name__ == '__main__':
    main()