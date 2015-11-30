#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import jieba
    print "[jieba] module had been installed"
except ImportError:
    print "[jieba] module is not installed"
    
try:
    import configobj
    print "[configobj] module had been installed"
except ImportError:
    print "[configobj] module is not installed"