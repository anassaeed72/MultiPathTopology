"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

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
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, switch1 )
        self.addLink( switch1, switch2 )
        self.addLink(switch2,switch3)
        self.addLink( switch3, rightHost )

        # self.addLink(switch1, switch2)
        # self.addLink(switch1, switch3)
        # self.addLink(switch2, switch5)
        self.addLink(switch3, switch4)
        # self.addLink(switch3, switch6)
        self.addLink(switch4, switch5)
        # self.addLink(switch4, switch7)
        # self.addLink(switch4, switch8)
        self.addLink(switch5, switch6)
        self.addLink(switch6, switch7)
        # self.addLink(switch6, switch8)
        self.addLink(switch7, switch8)
        # self.addLink(switch7, switch11)
        self.addLink(switch8, switch9)
        self.addLink(switch9, switch10)
        # self.addLink(switch9, switch11)
        self.addLink(switch10, switch11)
        # self.addLink(switch10, switch12)
        self.addLink(switch11, switch12)




        # self.addLink( leftHost, leftSwitch )
        # self.addLink( leftSwitch, rightSwitch )
        # self.addLink( rightSwitch, rightHost )


topos = { 'starter': ( lambda: MyTopo() ) }
