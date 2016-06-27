from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
import random
import os
import sys
class MultiPathRouting(Topo):
    def build(self):
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch5 = self.addSwitch('s5')
        switch6 = self.addSwitch('s6')
        switch7 = self.addSwitch('s7')
        switch8 = self.addSwitch('s8')
        switch9 = self.addSwitch('s9')
        switch10 = self.addSwitch('s10')
        switch11 = self.addSwitch('s11')
        switch12 = self.addSwitch('s12')
        
        self.addLink(switch1, switch2)
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
        self.addLink(switch8, switch10)
        self.addLink(switch9, switch10)
        self.addLink(switch9, switch11)
        self.addLink(switch10, switch11)
        self.addLink(switch10, switch12)
        self.addLink(switch11, switch12)

        clientHost1 = self.addHost('ch1')
        clientHost2 = self.addHost('ch3')
        clientHost3 = self.addHost('ch2')

        serverHost1 = self.addHost('sh1')
        serverHost1 = self.addHost('sh2')
        serverHost1 = self.addHost('sh3')

        listOfSwitches = random.sample(range(1,13),6)

        # for switch in listOfSwitches:
        #     self.addLink(clientHost2,clientHost3)
def setUpNetwork():
    multiPathRoutingTopology = MultiPathRouting()
    multiPathRoutingNetwork = Mininet(multiPathRoutingTopology)
    multiPathRoutingNetwork.start()
    multiPathRoutingNetwork.getNodeByName('s1')
    connectHostsToNetwork(multiPathRoutingNetwork)
    print "Dumping host connections"
    dumpNodeConnections(multiPathRoutingNetwork.hosts)
    print "Testing network connectivity"
    multiPathRoutingNetwork.pingAll()
    # multiPathRoutingNetwork.stop()
    os.system("sudo mn")
def connectHostsToNetwork(network):
    listOfSwitches = random.sample(range(1,13),6)
    network.addLink(network.getNodeByName('s'+str(listOfSwitches[0])),network.getNodeByName('ch1'))
    network.addLink(network.getNodeByName('s'+str(listOfSwitches[1])),network.getNodeByName('ch2'))
    network.addLink(network.getNodeByName('s'+str(listOfSwitches[2])),network.getNodeByName('ch3'))

    network.addLink(network.getNodeByName('s'+str(listOfSwitches[3])),network.getNodeByName('sh1'))
    network.addLink(network.getNodeByName('s'+str(listOfSwitches[4])),network.getNodeByName('sh2'))
    network.addLink(network.getNodeByName('s'+str(listOfSwitches[5])),network.getNodeByName('sh3'))
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    setUpNetwork()