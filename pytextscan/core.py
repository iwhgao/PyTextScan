#!/usr/bin/python
# -*-* coding:utf8 -*-

'''
Created on 2015年12月15日

@author: Administrator
'''

import re
import jieba.posseg as pseg
import chardet

class Scanner(object):
    '''
    classdocs
    '''

    def __init__(self, strline):
        '''
        Constructor
        '''
        
        self.__content = strline
        
    def doScan(self):
        
        self.__content = self.scanCNName()
        self.__content = self.scanBankCardNo()
        self.__content = self.scanIdenNo()
        self.__content = self.scanPhoneNo()
        self.__content = self.scanEmailAddr()
        
        return self.__content

    def scanCNName(self):
        '''中文分词检测中文姓名并处理'''
    
        jiebaRes = pseg.cut(self.__content)
        
        for tmp in jiebaRes:
            tmp = tmp.encode('utf-8')
            m = re.findall('(.*?)\/nr', str(tmp))
            if m is not None and len(m) > 0:
                firstName = m[0].decode('utf-8')[0:1].encode('utf-8')
                self.__content = re.sub(m[0], firstName + '**', self.__content)
                
        return self.__content
    
    def scanBankCardNo(self):
        '''识别银行卡号并处理'''
    
        m = re.findall('\D(6\d{14,18})\D', self.__content)
        if m is not None and len(m) > 0:
            for one in m:
                startNum = one[0:6]
                endNum = one[-4:]
                self.__content = re.sub(one, '%s*********%s' % (startNum, endNum), self.__content)
                
        return self.__content
    
    def scanIdenNo(self):
        '''识别身份证号并处理'''
    
        m = \
            re.findall('\D([123456789]\d{5}((19)|(20))\d{2}((0[123456789])|(1[012]))((0[123456789])|([12][0-9])|(3[01]))\d{3}[Xx0-9])\D'
                       , self.__content)
        if m is not None and len(m) > 0:
            for one in m:
                if len(one[0]) < 18:
                    continue
                startNum = one[0][0]
                endNum = one[0][-1]
                self.__content = re.sub(one[0], '%s***************%s' % (startNum,
                           endNum), self.__content)
                
        return self.__content
    
    def scanPhoneNo(self):
        '''识别手机开户并处理'''
    
        m = re.findall('\D(1[3578]\d{9})\D', self.__content)
        if m is not None and len(m) > 0:
            for one in m:
                startNum = one[0:3]
                endNum = one[-2:]
                self.__content = re.sub(one, '%s******%s' % (startNum, endNum), self.__content)
                
        return self.__content
    
    def scanEmailAddr(self):
        '''识别邮箱地址并处理'''
    
        m = \
            re.findall('(([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+(\.[a-zA-Z]{2,3})+)'
                       , self.__content)
        if m is not None and len(m) > 0:
            for one in m:
                m1 = re.findall('(\w+)@', one[0])
                maskedOne = re.sub(m1[0], '%s******' % m1[0][0], one[0])
                self.__content = re.sub(one[0], maskedOne, self.__content)
                
        return self.__content
    
    
class Masker(object):
    '''
    classdocs
    '''

    def __init__(self, strline):
        '''
        Constructor
        '''
        
        self.__content = strline
        
    def doMask(self):
        '''
        '''
        
        self.__content = self.maskCNName()
        self.__content = self.maskBankCardNo()
        self.__content = self.maskIdenNo()
        self.__content = self.maskPhoneNo()
        self.__content = self.maskEmailAddr()
        
        return self.__content

    def maskCNName(self):
        '''
                            中文分词检测中文姓名并处理
        '''
    
        jiebaRes = pseg.cut(self.__content)
        for tmp in jiebaRes:
            tmp =  tmp.encode('utf-8')
            m = re.findall('(.*?)\/nr', str(tmp))
            if m is not None and len(m) > 0:
                firstName = m[0].decode('utf-8')[0:1].encode('utf-8')
                self.__content = re.sub(m[0].decode('utf-8').encode('utf-8'), firstName + '**', self.__content)
                
        return self.__content
    
    def maskBankCardNo(self):
        '''识别银行卡号并处理'''
    
        m = re.findall('\D(6\d{14,18})\D', self.__content)
        if m is not None and len(m) > 0:
            for one in m:
                startNum = one[0:6]
                endNum = one[-4:]
                self.__content = re.sub(one, '%s*********%s' % (startNum, endNum), self.__content)
                
        return self.__content
    
    def maskIdenNo(self):
        '''识别身份证号并处理'''
    
        m = \
            re.findall('\D([123456789]\d{5}((19)|(20))\d{2}((0[123456789])|(1[012]))((0[123456789])|([12][0-9])|(3[01]))\d{3}[Xx0-9])\D'
                       , self.__content)
        if m is not None and len(m) > 0:
            for one in m:
                if len(one[0]) < 18:
                    continue
                startNum = one[0][0]
                endNum = one[0][-1]
                self.__content = re.sub(one[0], '%s***************%s' % (startNum,
                           endNum), self.__content)
                
        return self.__content
    
    def maskPhoneNo(self):
        '''识别手机开户并处理'''
    
        m = re.findall('\D(1[3578]\d{9})\D', self.__content)
        if m is not None and len(m) > 0:
            for one in m:
                startNum = one[0:3]
                endNum = one[-2:]
                self.__content = re.sub(one, '%s******%s' % (startNum, endNum), self.__content)
                
        return self.__content
    
    def maskEmailAddr(self):
        '''识别邮箱地址并处理'''
    
        m = \
            re.findall('(([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+(\.[a-zA-Z]{2,3})+)'
                       , self.__content)
        if m is not None and len(m) > 0:
            for one in m:
                m1 = re.findall('(\w+)@', one[0])
                maskedOne = re.sub(m1[0], '%s******' % m1[0][0], one[0])
                self.__content = re.sub(one[0], maskedOne, self.__content)
                
        return self.__content
    