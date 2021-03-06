# -*- coding: UTF8 -*-

from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor

from configobj import ConfigObj

class Echo(Protocol):
    def sendData(self):
        data = raw_input('> ')
        data = data.strip()
        
        if data is not None or data == 'exit':
            self.transport.write('Bye')
            self.transport.loseConnection()
        else:
            self.transport.write(data)
            
    def dataReceived(self, data):
        print data
        self.sendData()
        
    def connectionMade(self):
        self.sendData()
        
    def connectionLost(self, reason):
        print "Connection lost"
        
class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print 'Started to connect.'
   
    def buildProtocol(self, addr):
        print 'Connected.'
        return Echo()
   
    def clientConnectionLost(self, connector, reason):
        print 'Lost connection. Reason:', reason
   
    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason
        self.transport.loseConnection()

conf_ini = "../conf/PyTextScan-Client.ini"
config = ConfigObj(conf_ini,encoding='UTF8')

host = str(config['server']['servername'])
port = int(config['server']['serverport'])

reactor.connectTCP(host, port, EchoClientFactory()) #@UndefinedVariable
reactor.run() #@UndefinedVariable