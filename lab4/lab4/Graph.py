
'''
Demonstration of some simple graph algorithms.
    
@author: Jingsai Liang
'''

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

    '''
    Begins the DFS algorithm.
    '''
    def DFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    # this is the recursive version of DFS
    # mark each vertext as visited
    def DFS(self, method):
        self.DFSInit()
        if method == 'recursive':
            # Your code goes here:
            for vertex in self.vertices:
                if vertex in self.unVisitedVertices:
                    self.DFS_recur(vertex)

        elif method == 'stack':
            for vertex in self.vertices:
                if vertex in self.unVisitedVertices:
                    self.DFS_stack(vertex)
        return self.path
            

    def DFS_recur(self,vertex):
        # Your code goes here:
        # delete "pass" after writing your own code here 
        self.unVisitedVertices.remove(vertex)
        # self.path.append(vertex)
        self.path += vertex
        print(vertex)
        for child in self.adjacencyList[vertex]:
            if child in self.unVisitedVertices:
                self.DFS_recur(child)

        print(self.path)
            
    # this implementation of DFS uses a stack rather than recursion      
    def DFS_stack(self, vertex):
        stack = [vertex]
        while stack:
            vertex = stack.pop()
            if vertex in self.unVisitedVertices:
                self.unVisitedVertices.remove(vertex)
                self.path += vertex
                for child in self.adjacencyList[vertex]:
                    if child in self.unVisitedVertices:
                        stack.append(child)


    def BFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""
        

    def BFS(self):
        self.BFSInit()
        for vertex in self.vertices:
            if vertex in self.unVisitedVertices:
                self.BFS_queue(vertex)
        return self.path

    def BFS_queue(self, vertex):
        queue = [vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex in self.unVisitedVertices:
                self.unVisitedVertices.remove(vertex)
                self.path += vertex
                for child in self.adjacencyList[vertex]:
                    if child in self.unVisitedVertices:
                        queue.append(child)
 
        return self.path


    def hasCycle(self):
        # dfs search
        self.DFSInit()
        # create immediate parent dictionary
        ImmediateParent = {}
        # iterate through all vertex
        for vertex in self.vertices:
            if vertex in self.unVisitedVertices and self.isCycle(vertex, ImmediateParent):
                return True
        return False

    def isCycle(self, vertex, ImmediateParent):
        # mark current vertex 
        self.unVisitedVertices.remove(vertex)
        # iterate through children
        for child in self.adjacencyList[vertex]:
            if child in self.unVisitedVertices:
                ImmediateParent[child] = vertex
                # if a cycle is detected return True
                if self.isCycle(child, ImmediateParent):
                    return True
            elif ImmediateParent.get(vertex) != child:
                # a back edge 
                return True
        return False




       
                    
    # Work on this function for at most 10 extra points
    # def shortestpath(self, p, q):
        # Your code goes here:
       # pass # delete "pass" after writing your own code here 
  
                
        

        

