class TopologicalSorting:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a directed graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
        # file name
        self.name = fileName
        
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
        self.paths = 0

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

        # sorted list
        self.sortedList = []

    def print_and_save(self):
        #print(self.vertices)
        #print(self.adjacencyList)
        self.sort()
        print(self.sortedList)
        with open('result_'+str(self.name), 'w') as file_handler:
            for node in self.sortedList:
                file_handler.write("{}\n".format(node)) 
        

    # Topological sorting using decrease-by-one-and-conquer. 
    def sort(self):
        # dictionary to store number of parents/dependencies for each node
        parent_count = dict.fromkeys(self.vertices, 0)
        # count the number of parents for each node
        for parent in self.adjacencyList:
            for child in self.adjacencyList[parent]:
                parent_count[child] += 1
        # nodes with no parents
        available_nodes = [node for node in self.vertices if parent_count[node] == 0]
        while available_nodes:
            # add to the sorted list for nodes sithout dependencies
            current = available_nodes.pop(0)
            self.sortedList.append(current)

            if current in self.adjacencyList:
                for child in self.adjacencyList[current]:
                    parent_count[child] -= 1
                    if parent_count[child] == 0:
                        available_nodes.append(child)
        # if there is a cycle in the graph and not all nodes are added to the sorted list
        if len(self.sortedList) != len(self.vertices):
            raise ValueError("Cycle detected in the graph")


    # How many different ways can the spider reach the fly by moving along the web’s lines in the directions indicated by the arrow?
    def spider(self, start, end, visited=None):
        if visited is None:
            visited = set()

        if start == end:
            return 1
        else:
            visited.add(start)
            count = 0
            for vertex in self.adjacencyList.get(start, []):
                if vertex not in visited:
                    count += self.spider(vertex, end, visited.copy())
            return count


if __name__ == "__main__":

    s = TopologicalSorting("graph_example.txt")
    s.print_and_save()

    # Be careful! graph-courses.txt is incomplete. Please finish this txt file at first. 
    s = TopologicalSorting("graph_courses.txt")
    s.print_and_save()

    s = TopologicalSorting("graph_spider.txt")
    s.print_and_save()

    print(s.spider(s.sortedList[0], s.sortedList[-1]))



    