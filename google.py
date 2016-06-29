#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import OVSSwitch, OVSKernelSwitch, Controller, RemoteController
import random
import os
import sys
from mininet.cli import CLI
def myNetwork():

    net = Mininet( topo=None,
                   build=False, controller=RemoteController)

    info( '*** Adding controller\n' )

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1')
    Intf( 'eth2', node=s1 )

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip='0.0.0.0')

    info( '*** Add links\n')
    net.addLink(h1, s1)

    info( '*** Starting network\n')
    net.start()
    # h1.cmdPrint('dhclient '+h1.defaultIntf().name)
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()