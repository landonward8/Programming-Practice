from bridges.graph_adj_list import *
import heapq

# landon ward

class Dijkstra():
    def __init__(self, inputFile, startingVertex, goalVertex):
        # an initially empty dictionary containing mapping: vertex: [child, weight]
        self.adjacency = {}
        # collection of vertices
        self.vertices = []
        # each dictionary entry contains mapping of vertex:parent
        self.parent = {}
        # startingVertex, goalVertex
        self.startingVertex, self.goalVertex = startingVertex, goalVertex

        # The following reads in the input file and constructs an adjacency list of the graph.
        graph = open(inputFile)
        for line in graph:
            entry = line.split()

            # get the vertices
            self.vertices.append(entry[0])
            self.vertices.append(entry[1])

            if entry[0] not in self.adjacency:
                self.adjacency[entry[0]] = []

            # construct an edge for the adjacency list
            edge = (entry[1], int(entry[2]))
            self.adjacency[entry[0]].append(edge)

        # remove duplication in vertices
        self.vertices = list(set(self.vertices))

        # checking if start and goal are in vertices
        if startingVertex not in self.vertices:
            print('Starting vertex', startingVertex, 'not present in graph')
            quit()
        elif goalVertex not in self.vertices:
            print('Goal vertex', goalVertex, 'not present in graph')
            quit()

        # create Bridges graph
        self.g = GraphAdjList()
        for vertex in self.vertices:
            self.g.add_vertex(vertex, str(vertex))
            self.g.get_visualizer(vertex).color = "red"
        
        for vertex in self.adjacency:
            for edge in self.adjacency[vertex]:
                self.g.add_edge(vertex, edge[0], edge[1])

    # solve it using Dijkstra algorithm
    def solve(self):
       # your code goes here:
       # initialize a heap using the start vertex
       # distance as infinity

       fringe = []
       visted = []
       heapq.heappush(fringe, (0, self.startingVertex, None))
       
       while fringe: 
          priority, vertex, _ = heapq.heappop(fringe)
          for edge, weight in self.adjacency[vertex]:
            if vertex in visted:
                continue
                # need the cost of the edge
                # child is a string and the weight is an int, index 0 is the child, index 1 is the weight
            self.parent[edge] = vertex
            heapq.heappush(fringe, (priority + weight, edge, vertex))
            print(fringe)
            if edge == self.goalVertex:
                return True

                  

    # retrieve the path from start to the goal 
    def find_path(self):
        node = self.goalVertex
        self.path = [node]
        # your code goes here:
        while node != self.startingVertex:
            self.path.append(self.parent[node])
            node = self.parent[node]
        self.path = self.path[::-1]
                
    # draw the path as red
    def draw_path(self):
        print(self.path)
        for i in range(len(self.path)-1):
            self.g.get_link_visualizer(self.path[i], self.path[i+1]).color = "red"

    # return the Bridges object
    def get_graph(self):
        return self.g
