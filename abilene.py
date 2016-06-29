#!/usr/bin/python

from __future__ import print_function

import sys
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo, SingleSwitchTopo, LinearTopo
from mininet.topolib import TreeTopo
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info

class Abilene(Topo):
    def __init__(self, **opts):
        super(Abilene, self).__init__(**opts)

        self.h1 = self.addHost('h1', ip='0.0.0.0')
        self.h2 = self.addHost('h2', ip='0.0.0.0')
        self.h3 = self.addHost('h3', ip='0.0.0.0')
        self.h4 = self.addHost('h4', ip='0.0.0.0')
        self.h5 = self.addHost('h5', ip='0.0.0.0')
        self.h6 = self.addHost('h6', ip='0.0.0.0')
        self.h7 = self.addHost('h7', ip='0.0.0.0')
        self.h8 = self.addHost('h8', ip='0.0.0.0')
        self.h9 = self.addHost('h9', ip='0.0.0.0')
        self.h10 = self.addHost('h10', ip='0.0.0.0')
        self.h11 = self.addHost('h11', ip='0.0.0.0')

        self.s1 = self.addSwitch('s1', protocols='OpenFlow13')
        self.s2 = self.addSwitch('s2', protocols='OpenFlow13')
        self.s3 = self.addSwitch('s3', protocols='OpenFlow13')
        self.s4 = self.addSwitch('s4', protocols='OpenFlow13')
        self.s5 = self.addSwitch('s5', protocols='OpenFlow13')
        self.s6 = self.addSwitch('s6', protocols='OpenFlow13')
        self.s7 = self.addSwitch('s7', protocols='OpenFlow13')
        self.s8 = self.addSwitch('s8', protocols='OpenFlow13')
        self.s9 = self.addSwitch('s9', protocols='OpenFlow13')
        self.s10 = self.addSwitch('s10', protocols='OpenFlow13')
        self.s11 = self.addSwitch('s11', protocols='OpenFlow13')

        linkopts_1 = {'bw':100, 'delay':'1ms'}
        # linkopts_2 = {'bw':200, 'delay':'1ms'}

        self.addLink(self.h1, self.s1, **linkopts_1)
        self.addLink(self.h2, self.s2, **linkopts_1)
        self.addLink(self.h3, self.s3, **linkopts_2)
        self.addLink(self.h4, self.s4, **linkopts_1)
        self.addLink(self.h5, self.s5, **linkopts_1)
        self.addLink(self.h6, self.s6, **linkopts_1)
        self.addLink(self.h7, self.s7, **linkopts_1)
        self.addLink(self.h8, self.s8, **linkopts_1)
        self.addLink(self.h9, self.s9, **linkopts_1)
        self.addLink(self.h10, self.s10, **linkopts_1)
        self.addLink(self.h11, self.s11, **linkopts_1)
        self.addLink(self.s1, self.s2, **linkopts_1)
        self.addLink(self.s1, self.s3, **linkopts_1)
        self.addLink(self.s2, self.s3, **linkopts_1)
        self.addLink(self.s3, self.s4, **linkopts_1)
        self.addLink(self.s4, self.s5, **linkopts_1)
        self.addLink(self.s5, self.s6, **linkopts_1)
        self.addLink(self.s6, self.s7, **linkopts_1)
        self.addLink(self.s2, self.s8, **linkopts_1)
        self.addLink(self.s8, self.s9, **linkopts_1)
        self.addLink(self.s9, self.s10, **linkopts_1)
        self.addLink(self.s3, self.s8, **linkopts_1)
        self.addLink(self.s4, self.s9, **linkopts_1)
        self.addLink(self.s5, self.s10, **linkopts_1)
        self.addLink(self.s7, self.s11, **linkopts_1)
        self.addLink(self.s10, self.s11, **linkopts_1)

def myNetwork(arg):

    net = Mininet(Abilene(), switch=OVSKernelSwitch, controller=None, link=TCLink)
    net.addController(RemoteController( name='c0', ip='192.168.56.1' ))

    net.start()
    for ihost in net.hosts:
        if ihost.name[0] == 'h':
            ihost.cmdPrint('sudo ip add flush '+ ihost.defaultIntf().name)
            ihost.cmdPrint('dhclient '+ ihost.defaultIntf().name)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork(sys.argv)
