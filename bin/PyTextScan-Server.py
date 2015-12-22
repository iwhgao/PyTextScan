#!/usr/bin/python
# -*- coding: utf8 -*-

__author__ = 'deangao'
__version__ = '1.0.0'

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor
import logging.config
from pytextscan import core

class ProcessText(Protocol):
    '''
    classdocs
    '''
    
    def __init__(self, logger):
        '''
        Constructor
        '''
        self.logger = logger
        self.masker = core.Masker()
        
    def connectionMade(self):
        self.logger.debug("Connection comes from %s" % str(self.transport.getPeer()))
        
    def dataReceived(self, data):
        data = data.strip()
        self.transport.write('Received')
        processedData = self.masker.doMask(data)
        self.transport.write(processedData)
        
        self.logger.debug('Data content(from %s): %s' % (str(self.transport.getPeer()),data))
        self.logger.debug('Processed Data content(from %s): %s' % (str(self.transport.getPeer()),processedData))

    def connectionLost(self, reason='asdf'):
        print "Coonection lost from %s" % (str(self.transport.getPeer()))
        
class ProcessTextFactory(Factory):
    '''
    '''
    
    def __init__(self):
        logging.config.fileConfig("../conf/logger.conf")
        self.logger = logging.getLogger("pytextscan")
        self.logger.debug('PyTextScan Server is initialized')
    
    def buildProtocol(self, addr):  
        return ProcessText(self.logger) 
    
reactor.listenTCP(8124, ProcessTextFactory()) #@UndefinedVariable
reactor.run() #@UndefinedVariable