# find the minimum spanning tree
# This function is equivelent to Mathematica function FindSpanningTree

import math

def find_spanning_tree(graph,start_node):

    vertex =  list(graph.keys())

    S = [] # the growing tree

    open_nodes = {node:[None,math.inf] for node in vertex} # unconnected nodes
    open_nodes.pop(start_node, None) # remove the start node
    current_node = start_node # the current node

    while open_nodes != {}:
        for node in open_nodes:
            if node in graph[current_node]:
                if graph[current_node][node] < open_nodes[node][1]: # the node can be reached with shorter distance
                    open_nodes[node] = [current_node,graph[current_node][node]] # update the short distance

        next_node = min(open_nodes.items(),key = lambda x: x[1][1])[0] # the node with a minimum distance to S, will be select as best node

        S.append([open_nodes[next_node][0],next_node]) # add the link to S
        current_node = next_node # set the best node for next iteration
        open_nodes.pop(current_node,None) # remove the the best node from the unconnected nodes

    return S


# example 1

# graph = {
#     'A':{'B':1,'C':4,'E':1},
#     'B':{'A':1,'C':2,'D':3,'E':10,'F':3},
#     'C':{'A':4,'B':2,'D':3,'E':2},
#     'D':{'B':3,'C':3,'E':7,'F':3},
#     'E':{'A':1,'B':10,'C':2,'D':7},
#     'F':{'B':3,'D':3}
# }

# find_spanning_tree(graph,'A')

# example 2 from Mathematica documentation

#A company is planning a fiber network for a number of Chicago suburbs. It only has the right of way for its fiber along certain corridors. Some of those corridors might be more expensive. Find the subgraph of connection corridors that connect every suburb with the lowest total cost:

graph = {
    "Maywood":{"Downers":14, "Oakbrook":28, "Addison":10},
    "Downers":{"Maywood":14, "Oakbrook":27,"Grove":25, "Stickney":23, "Wheaton":20},
    "Oakbrook":{"Maywood":28, "Downers":27,"Addison":17, "Stickney":11},
    "Addison":{"Maywood":10, "Oakbrook":17, "McCook":21},
    "Grove":{"Downers":25,"Wheaton":10},
    "Stickney":{"Downers":23, "Oakbrook":11,"Wheaton":15, "Bellwood":20},
    "Wheaton":{"Downers":20,"Grove":10, "Stickney":15, "Bellwood":10},
    "Bellwood":{"Stickney":20, "Wheaton":10,"McCook":28},
    "McCook":{"Addison":21, "Bellwood":28}
    }


find_spanning_tree(graph, 'McCook')
