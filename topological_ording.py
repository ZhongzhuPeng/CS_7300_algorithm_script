graph = {'A': ['C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['E','F'],
         'E': ['G', 'H'],
         'F': ['H'],
         'G': ['H', 'I'],
         'H': [],
         'I': []
}

graph2 ={

    'a':['c','d','i'],
    'b':['c'],
    'c':['d','e','f'],
    'd':['e','f','h'],
    'e':['g'],
    'f':['h'],
    'g':[],
    'h':[],
    'i':['e']

}

graph3 = {

    'c':{'d':-5,'e':9,'f':-3},
    'd':{'e':1,'f':1,'h':1},
    'e':{'g':-2},
    'f':{'h':2},
    'g':{},
    'h':{}

}

def top_ord(graph):
    """calculate the topological ording of a graph"""

    #vertex of the graph
    vertex = graph.keys()

    #dict to record the indegree of each node
    indeg={node:0 for node in graph}
    for node in graph:
        for adj in graph[node]:
            indeg[adj] += 1

    #list of all nodes with zero indegree
    zero_indeg = [node for node in vertex if indeg[node]==0 ]

    #list to hold the topological ording
    topording=[]

    while(len(zero_indeg)>0):
        #select out a zero indegree node
        #add it to the topological ording
        x = zero_indeg.pop()
        topording.append(x)
        #update the indegree for its adjences
        #add the adjence to zero indgree list if its indegree is zero
        for y in graph[x]:
            indeg[y] -= 1
            if indeg[y] ==0 :
                zero_indeg.append(y)

    return topording



def reduce(graph,head):
    """reduce the graph so that the subgraph returned contains
    all the nodes that are reachable from x
    """

    #vertex of the graph
    vertex = graph.keys()

    #dict to record the indegree of each node
    indeg={node:0 for node in graph}
    for node in graph:
        for adj in graph[node]:
            indeg[adj] += 1

    #dict to hold the flag whether a node will be deleted or not
    eliminated = {node:0 for node in graph}

    #list of all nodes with zero indegree
    zero_indeg = [node for node in vertex if indeg[node]==0 ]

    #list to hold the topological ording
    topording=[]

    while(len(zero_indeg)>0):

        if zero_indeg == [head]:
            break

        if zero_indeg[-1] != head:
            x = zero_indeg.pop()
        else:
            x = zero_indeg.pop(-2)

        eliminated[x] = 1
        topording.append(x)

        for y in graph[x]:
            indeg[y] -= 1
            if indeg[y] ==0 :
                zero_indeg.append(y)

    #print(eliminated)

    return {node:graph[node] for node in graph if eliminated[node]==0}


def longestPathLength(graph,head):
    """return the dict holding the longest path length from the head to each node"""


    #dict to record the indegree of each node
    indeg={node:0 for node in graph}
    for node in graph:
        for adj in graph[node]:
            indeg[adj] += 1

    #initialize with head node
    zero_indeg = [head]

    #dict holding the longest path for each node
    L = {node:None for node in graph}

    #initialize the path length dict
    L[head] = 0
    S = 1
    for nodeX in graph:
        for nodeY in graph[nodeX]:
            S += abs(graph[nodeX][nodeY])

    for node in graph:
        if node == head:
            L[node] = 0
        else:
            L[node] = -S

    # loop through nodes with zero indgree
    while(len(zero_indeg)>0):

        x = zero_indeg.pop()

        for y in graph[x]:
            indeg[y] -= 1
            if indeg[y] ==0 :
                zero_indeg.append(y)
            #print('%s->%s,%d->%d'%(x,y,L[y],max(L[y],L[x]+graph[x][y])))
            L[y] = max(L[y],L[x]+graph[x][y])

    return L
