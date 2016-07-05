import dijkstra

listOfHostNamesAndMacs ={'ch1':"00:00:00:00:10:00",'ch2':"00:00:00:00:10:01",'ch3':"00:00:00:00:10:02",
							'sh1':"00:00:00:00:10:03",'sh2':"00:00:00:00:10:04",'sh3':"00:00:00:00:10:05"}
listOfMacs=['00','01','02','03','04','05']

listPath = ['ch1', 's1', 's2', 'ch2']
listPorts = {'s1-s2':1,'s2-s3':2,'s3-s4':2,'s4-s5':2,'s5-s6':2,'s6-s7':2,'s7-s8':2,
			's8-s9':2,'s9-s10':2,'s10-s11':2,'s11-s12':2,'s1-ch1':2,'s2-ch2':3,'s3-ch3':3,
			's4-sh1':3,'s5-sh2':3,'s6-sh3':3,
			's2-s1':1,'s3-s2':1,'s4-s3':1,'s5-s4':1,'s6-s5':1,'s7-s6':1,'s8-s7':1,'s9-s8':1,'s10-s9':1,'s11-s10':1,'s12-s11':1,
			's1-s2':1,
's1-s3':2 ,'s2-s3':2,'s2-s5':3,'s3-s4':3,'s3-s6':4,'s4-s5':2,'s4-s7':3,'s5-s6':3,
's6-s8':3,'s7-s8':2,'s7-s11':3,'s8-s9':3,'s9-s10':2,'s9-s11':3,'s10-s11':2,'s10-s12':3,
's11-s12':4,'s1-ch1':3,'s2-ch2':4,'s3-ch3':5,'s4-sh1':4,'s5-sh2':4,'s6-sh3':4,'s2-s1':1,
's3-s1':2,'s3-s2':1,'s5-s2':1,'s4-s3':1,'s6-s3':1,'s5-s4':2,'s7-s4':1,'s6-s5':2,
's8-s6':1,'s8-s7':2,'s11-s7':1,'s9-s8':1,'s10-s9':1,'s11-s9':2,'s11-s10':3,'s12-s10':1,
's12-s11':2,'ch1-s1':0,'ch2-s2':0,'ch3-s3':0,'sh1-s4':0,'sh2-s5':0,'sh3-s6':0}

def findPort(currentSwitch,nextSwitch):
	stringToFind = currentSwitch+"-"+nextSwitch
	return listPorts.get(stringToFind)

def findMacOfHost(hostName):
	return listOfHostNamesAndMacs.get(hostName)
def findRules(listPath):
	startMACParameter  = findMacOfHost(listPath[0])
	endMACParameter = findMacOfHost(listPath[-1])
	count = 0
	for switch in listPath:
		if count == 0 or count == len(listPath) -1:
			count = count +1
			continue
		count = count +1
		# if findPort(switch,listPath[count])  is None:
		# 	continue
		print "if str(nameOfSwitch)=='"+switch+"':"
		print "  self.installRuleBasedOnMac(\""+endMACParameter+"\","+str(findPort(switch,listPath[count]))+",event.connection)"
	count = 0
	# for switch in reversed(listPath):
	# 	if count == 0 or count == len(listPath) -1:
	# 		count = count +1
	# 		continue
	# 	count = count +1
	# 	print "if str(nameOfSwitch)[0:6]=='"+switch+"-eth':"
	# 	print "  self.installRuleBasedOnMac(\""+startMACParameter+"\","+str(findPort(switch,listPath[count-1]))+",event.connection)"


# pathFromStartToEnd = dijkstra.performDijkstraAndReturnPath('ch1','ch2')
# # print pathFromStartToEnd
# findRules(pathFromStartToEnd)

# pathFromStartToEnd = dijkstra.performDijkstraAndReturnPath('ch2','ch1')
# # print pathFromStartToEnd
# findRules(pathFromStartToEnd)
# # print dijkstra.performDijkstraAndReturnPath('ch1','ch2')

for startNode in listOfHostNamesAndMacs.keys():
	for endNode in listOfHostNamesAndMacs.keys():
		if startNode == endNode:
			continue
		pathFromStartToEnd = dijkstra.performDijkstraAndReturnPath(startNode,endNode)
		findRules(pathFromStartToEnd)