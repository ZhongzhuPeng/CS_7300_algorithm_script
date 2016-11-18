def dfs(graph, start):
    visited, stack = set(), [start]
    paths = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            paths.append(vertex)
            stack.extend(graph[vertex] - visited)
    return paths

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


graph2 = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def dfs_full(graph, start):
    visited, stack = [], [start]
    paths = []
    while stack:
        vertex = stack.pop()
        print "try (", vertex, graph[vertex][-1],")"
        if vertex not in visited:
            visited.append(vertex)
            paths.append(vertex)
            stack.extend([x for x in graph[vertex] if x not in visited])
    return paths
