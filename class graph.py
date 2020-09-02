# The Graph class contains a dictionary that maps vertex keys to vertex objects (vertlist) and a    count of the number of vertices in the graph
class Graph:

def __init__(self):
    self.vertList = {}
    self.numVertices = 0


# Returns a vertex which was added to the graph with given key
def addVertex(self,key):
    self.numVertices = self.numVertices + 1
    # create a vertex object
    newVertex = Vertex(key)
    # set its key
    self.vertList[key] = newVertex
    return newVertex

# Return the vertex object corresponding to the key - n
def getVertex(self,n):
    if n in self.vertList:
        return self.vertList[n]
    else:
        return None

# Returns boolean - checks if graph contains a vertex with key n
def __contains__(self,n):
    return n in self.vertList

# Add's an edge to the graph using addNeighbor method of Vertex
def addEdge(self,f,t,cost=0):
    # check if the 2 vertices involved in this edge exists inside
    # the graph if not they are added to the graph
    # nv is the Vertex object which is part of the graph
    # and has key of 'f' and 't' respectively, cost is the edge weight
    if f not in self.vertList:
        nv = self.addVertex(f)
    if t not in self.vertList:
        nv = self.addVertex(t)
    # self.vertList[f] gets the vertex with f as key, we call this Vertex
    # object's addNeighbor with both the weight and self.vertList[t] (the vertice with t as key) 
    self.vertList[f].addNeighbor(self.vertList[t], cost)

# Return the list of all key's corresponding to the vertex's in the graph
def getVertices(self):
    return self.vertList.keys()

# Returns an iterator object, which contains all the Vertex's
def __iter__(self):
    return iter(self.vertList.values())
