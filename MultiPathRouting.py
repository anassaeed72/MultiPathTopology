from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import OVSSwitch, OVSKernelSwitch, Controller, RemoteController
import random
import os
import sys
from mininet.cli import CLI
import thread
class MultiPathRouting(Topo):
    def build(self):
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        switch4 = self.addSwitch( 's4' )
        switch5 = self.addSwitch( 's5' )
        switch6 = self.addSwitch( 's6' )
        switch7 = self.addSwitch( 's7' )
        switch8 = self.addSwitch( 's8' )
        switch9 = self.addSwitch( 's9' )
        switch10 = self.addSwitch( 's10' )
        switch11 = self.addSwitch( 's11' )
        switch12 = self.addSwitch( 's12' )

        
        # Add hosts and switches
        # leftHost = self.addHost( 'h1' ,ip=None)
        # rightHost = self.addHost( 'h2' ,ip =None)
        listOfClientHosts=[]
        for ch in range(3):
            host = self.addHost('ch%s' % (ch + 1))
            listOfClientHosts.append(host)

        listOfServerHosts=[]
        for sh in range(3):
            host = self.addHost('sh%s' % (sh + 1))
            listOfServerHosts.append(host)


        # Add links
        # self.addLink( leftHost, switch1 )
        self.addLink( switch1, switch2 )
        self.addLink(switch2,switch3)
        # self.addLink( switch3, rightHost )


        self.addLink(switch1, switch3)
        self.addLink(switch2, switch5)
        self.addLink(switch3, switch4)
        self.addLink(switch3, switch6)
        self.addLink(switch4, switch5)
        self.addLink(switch4, switch7)
        self.addLink(switch4, switch8)
        self.addLink(switch5, switch6)
        self.addLink(switch6, switch7)
        self.addLink(switch6, switch8)
        self.addLink(switch7, switch8)
        self.addLink(switch7, switch11)
        self.addLink(switch8, switch9)
        self.addLink(switch9, switch10)
        self.addLink(switch9, switch11)
        self.addLink(switch10, switch11)
        self.addLink(switch10, switch12)
        self.addLink(switch11, switch12)

        

def setUpNetwork():
    multiPathRoutingTopology = MultiPathRouting()
    multiPathRoutingNetwork = Mininet(topo=multiPathRoutingTopology,controller=None)
    multiPathRoutingNetwork.addController( 'c0', controller=RemoteController, ip='0.0.0.0', port=6633 )
    connectNodesToNetwork(multiPathRoutingNetwork)
    multiPathRoutingNetwork.start()
    print "Dumping host connections"
    # connectServers(multiPathRoutingNetwork)
    # connnectEchoClient(multiPathRoutingNetwork)
     
    dumpNodeConnections(multiPathRoutingNetwork.hosts)
    getIpFromDHCPServer(multiPathRoutingNetwork)
    
    connectEchoServer(multiPathRoutingNetwork)
    connnectEchoClient(multiPathRoutingNetwork)
    CLI(multiPathRoutingNetwork)
    
    multiPathRoutingNetwork.stop()

def getIpFromDHCPServer(network):
    listOfNodes = ['ch1','ch2','ch3','sh1','sh2','sh3']
    for node in listOfNodes:
        nodeTemp  = network.getNodeByName(node)
        nodeTemp.cmdPrint('ifconfig ' + nodeTemp.defaultIntf().name +" 0")
        nodeTemp.cmdPrint('dhclient '+nodeTemp.defaultIntf().name)
        nodeTempIP = nodeTemp.cmd('ifconfig '+nodeTemp.defaultIntf().name)[79:92]
        nodeTemp.setIP(nodeTempIP)

def connectEchoServer(network):
    listOfServerHostsNames  = ['sh1','sh2','sh3']
    for serverNodeName in listOfServerHostsNames:
        serverNode = network.getNodeByName(serverNodeName)
        serverNodeIP = serverNode.cmd('ifconfig '+serverNode.defaultIntf().name)
        serverNodeIP =  serverNodeIP[79:92]
        serverNode.cmdPrint('python EchoServer.py '+str(serverNodeIP)+'&')
def connectNodesToNetwork(multiPathRoutingNetwork):
    listOfSwitchesForHosts = random.sample(range(1,13),6)
    for i in range(3):
        multiPathRoutingNetwork.addLink(multiPathRoutingNetwork.getNodeByName("s"+str(listOfSwitchesForHosts[i])),multiPathRoutingNetwork.getNodeByName('ch'+str(i+1)))

    for i in range(3):
        multiPathRoutingNetwork.addLink(multiPathRoutingNetwork.getNodeByName("s"+str(listOfSwitchesForHosts[i+3])),multiPathRoutingNetwork.getNodeByName('sh'+str(i+1)))


def connnectEchoClient(network):
    listOfClientHostsNames = ['ch1','ch2','ch3']
    listOfServerHostsNames  = ['sh1','sh2','sh3']
    for i in range(3):
        serverNode = network.getNodeByName(listOfServerHostsNames[i])
        clientNode = network.getNodeByName(listOfClientHostsNames[i])
        serverNodeIP = serverNode.cmd('ifconfig '+serverNode.defaultIntf().name)[79:92]
        clientNode.cmdPrint('python EchoClient.py '+str(serverNodeIP)+' 12321 &')
    # clientNode = network.getNodeByName('h2')
    # clientNodeIP = clientNode.cmd('ifconfig '+clientNode.defaultIntf().name)[79:92]
    # clientNode.cmdPrint('python EchoClient.py ')
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    setUpNetwork()