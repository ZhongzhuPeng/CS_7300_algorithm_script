lastDFSlabel = 1

graph = {'A': ['B', 'C', 'E', 'G'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D'],
         'D': ['B', 'C'],
         'E': ['A', 'F', 'G', 'H', 'I'],
         'F': ['E'],
         'G': ['A', 'E', 'H', 'I'],
         'H': ['E', 'G', 'I'],
         'I': ['E', 'G', 'H']
}

#{key: value.reverse() for (key,value) in graph.iteritems()}

vertex = ['A','B','C','D','E','F','G','H','I']

parent = {key:None for key in vertex}
dfsLabel = {key:None for key in vertex}
low = {key:None for key in vertex}
stack = []
child_num = 0


startNode = 'A'

def dfs(x):
    '''
    perform dfs search. print each step.
    '''
    global graph, parent, dfsLabel, lastDFSlabel

    if x == startNode:
        parent[x] = x
        dfsLabel[x] = 1
        lastDFSlabel = 1

    for y in graph[x]:
        if dfsLabel[y] == None:
            print "%s->%s 1st visit of a tree-edge" % (x,y)
            lastDFSlabel += 1
            dfsLabel[y] = lastDFSlabel
            parent[y] = x
            dfs(y)
        elif y == parent[x]:
            print "%s->%s 2nd visit of a tree-edge" % (x,y)
        elif dfsLabel[x] > dfsLabel[y]:
            print "%s->%s 1st visit of a back-edge" % (x,y)
        else:
            print "%s->%s 2nd visit of a back-edge" % (x,y)


def dfs_low(x):
    '''
    perform dfs search, calculate the low value for each vertex
    '''
    global graph, parent, dfsLabel, lastDFSlabel, low, stack, child_num

    if x == startNode:
        parent[x] = x
        dfsLabel[x] = 1
        lastDFSlabel = 1

    #initialize low value
    low[x] = dfsLabel[x]
    stack.insert(0,x)
    print "%s\t%i\t%s" %(x,low[x],str(stack))
    for y in graph[x]:
        if x == startNode:
            # root is cut-vertex after discover a second child
            child_num += 1
            if child_num == 2:
                print "%s is a cut-vertex\n" %(x)

        if dfsLabel[y] == None:
            #print "%s->%s 1st visit of a tree-edge" % (x,y)
            lastDFSlabel += 1
            dfsLabel[y] = lastDFSlabel
            parent[y] = x

            #visit y
            dfs_low(y)

            #after back track update low value of x
            #the low value of x is the min of its current low value and
            #the low value of its child
            low[x] = min(low[x],low[y])

        elif y == parent[x]:
            #print "%s->%s 2nd visit of a tree-edge" % (x,y)
            pass
        elif dfsLabel[x] > dfsLabel[y]:
            #print "%s->%s 1st visit of a back-edge" % (x,y)
            #the low value is min of current low value and the dfs label of
            #the backtrack vertex
            low[x] = min(low[x],dfsLabel[y])
        else:
            #print "%s->%s 2nd visit of a back-edge" % (x,y)
            pass

    # before backtrack, test whether the parent of x is cut-vertex
    # if low(x) < dfs label of parent(x) fails, then parent (x) is a cut-vertex
    # provided parent(x) is not root
    if low[x] >= dfsLabel[parent[x]]:
        if parent[x] != startNode:
            print "\n%s is a cut-vertex\n" % (parent[x])
        bicomp = stack[:stack.index(x)+1] + [parent[x]]
        stack = stack[stack.index(x)+1:]
        print "\nbicomp = %s\n" %(str(bicomp))





