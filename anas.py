from pox.core import core
from pox.lib.util import dpid_to_str
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str, str_to_dpid
from pox.lib.util import str_to_bool
import time
import socket, struct
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt

from pox.lib.addresses import IPAddr,EthAddr,parse_cidr
from pox.lib.addresses import IP_BROADCAST, IP_ANY
from pox.lib.revent import *
import dijkstra
from pox.proto.dhcpd import DHCPD

log = core.getLogger()
 
class MyComponent (object):
  listOfConnectedSwitches = []
  listOfHostNamesAndMacs ={'ch1':"00:00:00:00:10:00",'ch2':"00:00:00:00:10:01",'ch3':"00:00:00:00:10:02",'sh1':"00:00:00:00:10:03",'sh2':"00:00:00:00:10:04",'sh3':"00:00:00:00:10:05"}
  listPorts = {'s1-s2':1,'s2-s3':2,'s3-s4':2,'s4-s5':2,'s5-s6':2,'s6-s7':2,'s7-s8':2,'s8-s9':2,'s9-s10':2,'s10-s11':2,'s11-s12':2,'s1-ch1':2,'s2-ch2':3,'s3-ch3':3,'s4-sh1':3,'s5-sh2':3,'s6-sh3':3,'s2-s1':1,'s3-s2':1,'s4-s3':1,'s5-s4':1,'s6-s5':1,'s7-s6':1,'s8-s7':1,'s9-s8':1,'s10-s9':1,'s11-s10':1,'s12-s11':1,'s1-s2':1,'s1-s3':2 ,'s2-s3':2,'s2-s5':3,'s3-s4':3,'s3-s6':4,'s4-s5':2,'s4-s7':3,'s5-s6':3,'s6-s8':3,'s7-s8':2,'s7-s11':3,'s8-s9':3,'s9-s10':2,'s9-s11':3,'s10-s11':2,'s10-s12':3,'s11-s12':4,'s1-ch1':3,'s2-ch2':4,'s3-ch3':5,'s4-sh1':4,'s5-sh2':4,'s6-sh3':4,'s2-s1':1,'s3-s1':2,'s3-s2':1,'s5-s2':1,'s4-s3':1,'s6-s3':1,'s5-s4':2,'s7-s4':1,'s6-s5':2,'s8-s6':1,'s8-s7':2,'s11-s7':1,'s9-s8':1,'s10-s9':1,'s11-s9':2,'s11-s10':3,'s12-s10':1,'s12-s11':2,'ch1-s1':0,'ch2-s2':0,'ch3-s3':0,'sh1-s4':0,'sh2-s5':0,'sh3-s6':0}
  listOfRules = []
  def __init__ (self):
    core.openflow.addListeners(self)

    listTemp = []
    for x in xrange(13):
      self.listOfRules.append(listTemp)
    self.findAllRules()

  def _handle_LinkDiscovery(self,event):
    log.debug("Link Discovery event")
    log.debug(event.added)
    log.debug(event.link)
    
  def findAllRules(self):
    for startNode in self.listOfHostNamesAndMacs.keys():
      for endNode in self.listOfHostNamesAndMacs.keys():
        if startNode == endNode:
          continue
        self.findOneRule(startNode,endNode)
  def _handle_DHCPLease(self,event):
    print "IP leased fucntion called"
    print event.host_mac, event.ip, event._nak
  def findOneRule(self,startNode,endNode):
    pathBetweenNodes =dijkstra.performDijkstraAndReturnPath(startNode,endNode)
    count = 0
    for switch in pathBetweenNodes:
      if count == 0 or count == len(pathBetweenNodes) -1:
        count = count +1
        continue
      count = count +1
      rule = Rule()
      rule.switchName = switch
      rule.MAC =  self.findMacOfHost(pathBetweenNodes[-1])
      rule.port = self.findPort(switch,pathBetweenNodes[count])
      self.listOfRules[int(switch[1:])-1].append(rule)
  def findPort(self,currentSwitch,nextSwitch):
    stringToFind = currentSwitch+"-"+nextSwitch
    return self.listPorts.get(stringToFind)
  def findMacOfHost(self,hostName):

    return self.listOfHostNamesAndMacs.get(hostName)
  def installRule(self,IP,port,connection):
    log.debug("Installing rule dest IP " +IP +" port "+str(port))
    msg = of.ofp_flow_mod()
    msg.idle_timeout = 1000
    msg.hard_timeout = 3000
    msg.match.dl_type = 0x800
    msg.match.nw_dst = IP
    msg.actions.append(of.ofp_action_output(port = int(port)))
    connection.send(msg)
  def installRuleBasedOnMac(self,MAC,port,connection):
    log.debug("Installing rule dest MAC " +MAC +" port "+str(port))
    msg = of.ofp_flow_mod()
    msg.idle_timeout = 65535
    msg.hard_timeout = 65535
    msg.match.dl_dst = EthAddr(MAC)
    msg.actions.append(of.ofp_action_output(port = int(port)))
    connection.send(msg)
  def installListOfRules(self,rulesList,connection,nameOfSwitch):
    for rule in rulesList:
      if rule.switchName != nameOfSwitch:
        continue
      self.installRuleBasedOnMac(rule.MAC,int(rule.port),connection)
  def _handle_ConnectionUp (self, event):
    core.DHCPD.addListenerByName("DHCPLease", self._handle_DHCPLease)
    core.openflow_discovery.addListenerByName("LinkEvent", self._handle_LinkDiscovery)
    log.debug("Switch %s has come up.", dpid_to_str(event.dpid))
    nameOfSwitch = event.ofp.ports[0].name
    self.listOfConnectedSwitches.append(nameOfSwitch)
    self.installListOfRules(self.listOfRules[int(nameOfSwitch[1:])-1],event.connection,nameOfSwitch)
 
def launch ():

  core.registerNew(MyComponent)

class Rule(object):
  def __init__(self):
    self.switchName = "s"
    self.MAC="00:00:00:00:00:00"
    self.port=0
