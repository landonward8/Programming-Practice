import numpy as np
from heapq import heappush, heappop
from animation import draw
import argparse

# Landon Ward

class Node():
    """
    cost_from_start - the cost of reaching this node from the starting node
    state - the state (row,col)
    parent - the parent node of this node, default as None
    """
    def __init__(self, state, cost_from_start, parent = None):
        self.state = state
        self.parent = parent
        self.cost_from_start = cost_from_start


class Maze():
    
    def __init__(self, map, start_state, goal_state, map_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.map = map
        self.visited = [] # state
        self.m, self.n = map.shape 
        self.map_index = map_index


    def draw(self, node):
        path=[]
        while node.parent:
            path.append(node.state)
            node = node.parent
        path.append(self.start_state)
    
        draw(self.map, path[::-1], self.map_index)


    def goal_test(self, current_state):
        # your code goes here:
        return np.array_equal(current_state, self.goal_state)


    def get_cost(self, current_state, next_state):
        # your code goes here:
        return 1

    # get successor function
    def get_successors(self, state):
        successors = []
        row_change = [0, 0, -1, 1]
        col_change = [-1, 1, 0, 0]

        row, col = state 

        for i in range(4):
            new_row = row + row_change[i]
            new_col = col + col_change[i]

            if 0 <= new_row < self.m and 0 <= new_col < self.n and self.map[new_row, new_col] != 0:
                successors.append((new_row, new_col))

        return successors


    # heuristics function
    def heuristics(self, state):
        row = abs(state[0] - self.goal_state[0])
        col = abs(state[1] - self.goal_state[1])
        return row + col


    # priority of node 
    def priority(self, node):
        # your code goes here:
        return self.heuristics(node.state) + node.cost_from_start

    
    # solve it
    def solve(self):
        if self.goal_test(self.start_state):
            return

        current_state = tuple(self.start_state)
        self.visited.append(current_state)  
        root_node = Node(current_state, 0, None)  
        node_counter = 0  
        fringe = [(self.priority(root_node), node_counter, root_node)]  

        while fringe:
            _, _, current_node = heappop(fringe)  

            successors = self.get_successors(current_node.state)

            for successor_state in successors:
                successor_state = tuple(successor_state)

                if successor_state in self.visited:
                    continue

                self.visited.append(successor_state)  

                new_cost = current_node.cost_from_start + self.get_cost(current_node.state, successor_state)
                successor_node = Node(successor_state, new_cost, current_node)

                if self.goal_test(successor_state):
                    self.draw(successor_node)
                    return

                node_counter += 1 
                heappush(fringe, (self.priority(successor_node), node_counter, successor_node)) 


            
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='maze')
    parser.add_argument('-index', dest='index', required = True, type = int)
    index = parser.parse_args().index

    # Example:
    # Run this in the terminal solving map 1
    #     python maze_astar.py -index 1
    
    data = np.load('map_'+str(index)+'.npz')
    map, start_state, goal_state = data['map'], tuple(data['start']), tuple(data['goal'])

    game = Maze(map, start_state, goal_state, index)
    game.solve()
    