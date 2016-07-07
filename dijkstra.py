import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def initilize(self):
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    if start is None:
        print "Start is none"
        return
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
        heapq.heapify(unvisited_queue)

def performDijkstraAndReturnPath(startNode,endNode):
    g = Graph()

    g.add_vertex('s1')
    g.add_vertex('s2')
    g.add_vertex('s3')
    g.add_vertex('s4')
    g.add_vertex('s5')
    g.add_vertex('s6')
    g.add_vertex('s7')
    g.add_vertex('s8')
    g.add_vertex('s9')
    g.add_vertex('s10')
    g.add_vertex('s11')
    g.add_vertex('s12')

    g.add_vertex('ch1')
    g.add_vertex('ch2')
    g.add_vertex('ch3')

    g.add_vertex('sh1')
    g.add_vertex('sh2')
    g.add_vertex('sh3')

    g.add_edge('s1', 's2', 1)  
    g.add_edge('s2', 's3', 1)  
    g.add_edge('s1', 's3', 1)  
    g.add_edge('s2', 's5', 1)  
    g.add_edge('s3', 's4', 1)  
    g.add_edge('s3', 's6', 1)  
    g.add_edge('s4', 's5', 1)  
    g.add_edge('s4', 's7', 1)  
    g.add_edge('s5', 's6', 1)  
    g.add_edge('s6', 's7', 1)  
    g.add_edge('s6', 's8', 1)  
    g.add_edge('s7', 's8', 1)  
    g.add_edge('s7', 's11', 1)  
    g.add_edge('s8', 's9', 1)  
    g.add_edge('s9', 's10', 1)  
    g.add_edge('s9', 's11', 1)  
    g.add_edge('s10', 's11', 1)  
    g.add_edge('s10', 's12', 1)  
    g.add_edge('s11', 's12', 1)  

    g.add_edge('ch1', 's1', 1)  
    g.add_edge('ch2', 's2', 1)  
    g.add_edge('ch3', 's3', 1)  

    g.add_edge('sh1', 's4', 1)  
    g.add_edge('sh2', 's5', 1)  
    g.add_edge('sh3', 's6', 1)  

    return performDijkstraAndPrint(g,startNode,endNode)
def performDijkstraAndPrint(graph,startNode, endNode):
    print "Dijstra for "+ startNode +" -> " + endNode
    # dijkstra(graph, graph.get_vertex(startNode), graph.get_vertex(endNode)) 
    # target = graph.get_vertex(endNode)
    # if target is None:
    #     print "target is not found " + str( target) + " endNode " + str(endNode)
    #     print "Graph vertices ",graph.get_vertices()

    #     return
    # path = [target.get_id()]
    # shortest(target, path)
    # print 'The shortest path : %s' %(path[::-1])
    # return path
    dijkstra(graph, graph.get_vertex(startNode), graph.get_vertex(endNode)) 

    target = graph.get_vertex(endNode)
    if target is None:
        print "target is not found " + str( target) + " endNode " + str(endNode)
    #     print "Graph vertices ",graph.get_vertices()

        return
    path = [target.get_id()]
    shortest(target, path)
    # print 'Graph data:'
    # for v in graph:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))
    print 'The shortest path : %s' %(path[::-1])
    for vertices in graph.get_vertices():
        graph.get_vertex(vertices).initilize()
    return path

# if __name__ == '__main__':

#     g = Graph()

#     g.add_vertex('s1')
#     g.add_vertex('s2')
#     g.add_vertex('s3')
#     g.add_vertex('s4')
#     g.add_vertex('s5')
#     g.add_vertex('s6')
#     g.add_vertex('s7')
#     g.add_vertex('s8')
#     g.add_vertex('s9')
#     g.add_vertex('s10')
#     g.add_vertex('s11')
#     g.add_vertex('s12')

#     g.add_vertex('ch1')
#     g.add_vertex('ch2')
#     g.add_vertex('ch3')

#     g.add_vertex('sh1')
#     g.add_vertex('sh2')
#     g.add_vertex('sh3')

#     g.add_edge('s1', 's2', 1)  
#     g.add_edge('s2', 's3', 1)  
#     g.add_edge('s1', 's3', 1)  
#     g.add_edge('s2', 's5', 1)  
#     g.add_edge('s3', 's4', 1)  
#     g.add_edge('s3', 's6', 1)  
#     g.add_edge('s4', 's5', 1)  
#     g.add_edge('s4', 's7', 1)  
#     g.add_edge('s5', 's6', 1)  
#     g.add_edge('s6', 's7', 1)  
#     g.add_edge('s6', 's8', 1)  
#     g.add_edge('s7', 's8', 1)  
#     g.add_edge('s7', 's11', 1)  
#     g.add_edge('s8', 's9', 1)  
#     g.add_edge('s9', 's10', 1)  
#     g.add_edge('s9', 's11', 1)  
#     g.add_edge('s10', 's11', 1)  
#     g.add_edge('s10', 's12', 1)  
#     g.add_edge('s11', 's12', 1)  

#     g.add_edge('ch1', 's1', 1)  
#     g.add_edge('ch2', 's2', 1)  
#     g.add_edge('ch3', 's3', 1)  

#     g.add_edge('sh1', 's4', 1)  
#     g.add_edge('sh2', 's5', 1)  
#     g.add_edge('sh3', 's6', 1)  

#     # dijkstra(g, g.get_vertex('ch1'), g.get_vertex('ch2')) 

#     # target = g.get_vertex('ch2')
#     # path = [target.get_id()]
#     # shortest(target, path)
#     # print 'The shortest path : %s' %(path[::-1])
#     # print 'The shortest path : %s' %(path)
#     # print performDijkstraAndReturnPath('ch1','ch2')
#     # print performDijkstraAndPrint(g,'ch1','ch2')
#     print performDijkstraAndReturnPath('ch1','ch2')