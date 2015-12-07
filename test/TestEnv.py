#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Change the option prefix charaters')

parser.add_argument('-s', action='store', dest='simple_value', type=int,
        help='Store a simple value')

parser.add_argument('-c', action='store_const', dest='constant_value',
        const='value-to-store',
        help='Store a constant value')

parser.add_argument('-t', action='store_true', default=False,
        dest='boolean_switch',
        help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
        dest='boolean_switch',
        help='Set a switch to false')

parser.add_argument('-a', action='append', dest='collection',
        default=[],
        help='Add repeated values to a list')

parser.add_argument('-A', action='append_const', dest='const_collection',
        const='value-1-to-append',
        default=[],
        help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection',
        const='value-2-to-append',
        help='Add different values to list')

parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')
results = parser.parse_args()
print 'simple_value     =', results.simple_value
print 'constant_value   =', results.constant_value
print 'boolean_switch   =', results.boolean_switch
print 'collection       =', results.collection
print 'const_collection =', results.const_collection

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