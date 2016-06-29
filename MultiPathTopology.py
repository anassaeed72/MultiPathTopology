from mininet.topo import Topo
import random
class MultiPathTopology( Topo ):

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        listOfSwitches=[]
        for s in range(12):
            switch = self.addSwitch('s%s' % (s + 1))
            listOfSwitches.append(switch)
       
        self.addLink(listOfSwitches[0], listOfSwitches[1])
        self.addLink(listOfSwitches[0], listOfSwitches[2])
        self.addLink(listOfSwitches[1], listOfSwitches[4])
        self.addLink(listOfSwitches[2], listOfSwitches[3])
        self.addLink(listOfSwitches[2], listOfSwitches[5])
        self.addLink(listOfSwitches[3], listOfSwitches[4])
        self.addLink(listOfSwitches[3], listOfSwitches[6])
        self.addLink(listOfSwitches[3], listOfSwitches[7])
        self.addLink(listOfSwitches[4], listOfSwitches[5])
        self.addLink(listOfSwitches[5], listOfSwitches[6])
        self.addLink(listOfSwitches[5], listOfSwitches[7])
        self.addLink(listOfSwitches[6], listOfSwitches[7])
        self.addLink(listOfSwitches[6], listOfSwitches[10])
        self.addLink(listOfSwitches[7], listOfSwitches[9])
        self.addLink(listOfSwitches[8], listOfSwitches[9])
        self.addLink(listOfSwitches[8], listOfSwitches[10])
        self.addLink(listOfSwitches[9], listOfSwitches[10])
        self.addLink(listOfSwitches[9], listOfSwitches[11])
        self.addLink(listOfSwitches[10], listOfSwitches[11])
     
        listOfClientHosts=[]
        for ch in range(3):
            host = self.addHost('ch%s' % (ch + 1))
            listOfClientHosts.append(host)

        listOfServerHosts=[]
        for sh in range(3):
            host = self.addHost('sh%s' % (sh + 1))
            listOfServerHosts.append(host)

        listOfSwitchesForHosts = random.sample(range(1,13),6)
        
        self.addLink(listOfSwitches[listOfSwitchesForHosts[0]],listOfClientHosts[0])
        self.addLink(listOfSwitches[listOfSwitchesForHosts[1]],listOfClientHosts[1])
        self.addLink(listOfSwitches[listOfSwitchesForHosts[2]],listOfClientHosts[2])

        self.addLink(listOfSwitches[listOfSwitchesForHosts[3]],listOfServerHosts[0])
        self.addLink(listOfSwitches[listOfSwitchesForHosts[4]],listOfServerHosts[1])
        self.addLink(listOfSwitches[listOfSwitchesForHosts[5]],listOfServerHosts[2])


topos = { 'multiPathTopology': ( lambda: MultiPathTopology() ) }
