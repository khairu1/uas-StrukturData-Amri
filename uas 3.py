#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex] = edge
    
    def checkRoute(self, startNode, endNode):
        visited = []
        queue = [startNode]
        path = []
        if startNode == endNode:
            return [startNode]
        while queue:
            deVertex = queue.pop(0)
            if deVertex not in visited:
                visited.append(deVertex)
            else:
                continue
            if deVertex == endNode:
                path.append(deVertex)
                return path
            if self.gdict[deVertex]:
                path.append(deVertex)
                adjacentVertices = self.gdict[deVertex]
                for adjacentVertex in adjacentVertices:
                    queue.append(adjacentVertex)
        return None


customDict = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': [],
    'e': ['f'],
    'f': ['g'],
    'g': ['h'],
    'h': ['i'],
    'i': ['j'],
    'j': []
}

g = Graph(customDict)
print(g.checkRoute('a', 'j'))


# In[ ]:




