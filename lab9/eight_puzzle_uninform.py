import numpy as np
from animation import draw
import argparse
import heapq
from heapq import heappush, heappop

# landon ward --
# lab10

class Node():
    """
    cost_from_start - the cost of reaching this node from the starting node
    state - the state (row,col)
    parent - the parent node of this node, default as None
    """

    def __init__(self, state, cost_from_start, parent=None):
        self.state = state
        self.parent = parent
        self.cost_from_start = cost_from_start


class EightPuzzle():

    def __init__(self, start_state, goal_state, method, algorithm, array_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.visited = []  # state
        self.method = method
        self.algorithm = algorithm
        self.m, self.n = start_state.shape
        self.array_index = array_index

    # goal test function
    def goal_test(self, current_state):
        return np.array_equal(current_state, self.goal_state)

    # get cost function
    def get_cost(self, current_state, next_state):
        return 1

    # get successor function
    def get_successors(self, state):
        successors = []
        row_change = [0, 0, -1, 1]
        col_change = [-1, 1, 0, 0]

        empty_position = np.where(state == 0)
        empty_y, empty_x = empty_position[0][0], empty_position[1][0]

        for i in range(4):
            if ((empty_x + col_change[i] < self.n and empty_y + row_change[i] >= 0) and
                    (empty_x + col_change[i] >= 0 and empty_y + row_change[i] < self.m)):
            # if -1 < empty_x + row_change[i] <= self.m and -1 < empty_y + col_change[i] <= self.n:
                copy = state.copy()
                temp = copy[int(empty_y) + row_change[i]][int(empty_x) + col_change[i]]
                copy[int(empty_y) + row_change[i]][int(empty_x) + col_change[i]] = 0
                copy[int(empty_y)][int(empty_x)] = temp
                successors.append(copy)
        return successors

    # draw
    def draw(self, node):
        path = []
        while node.parent:
            path.append(node.state)
            node = node.parent
        path.append(self.start_state)
        draw(path[::-1], self.array_index, self.algorithm, self.method)
    
    def heuristics(self, state):
        cost = 0
        if self.method == 'Hamming':
            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] != self.goal_state[i][j]:
                        cost += 1
            return cost

        elif self.method == 'Manhattan':
            coordinates = {}
            for i in range(len(self.goal_state)):
                for j in range(len(self.goal_state[i])):
                    coordinates[self.goal_state[i][j]] = (i, j)

            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] != self.goal_state[i][j]:
                        x, y = np.where(self.goal_state == state[i][j])
                        cost += abs(x - i) + abs(y - j)
            return cost
        

    def priority(self, node):
        if self.algorithm == 'Greedy':
            return self.heuristics(node.state)
        elif self.algorithm == 'AStar':
            return self.heuristics(node.state) + node.cost_from_start

    # chat gpt did help me with some of the code to understand becuase I was not in class. Happy to explain it if needed.

    def solve(self):
        if self.goal_test(self.start_state):
            return

        current_state = self.start_state.copy()
        self.visited.append(current_state)
        root_node = Node(current_state, 0, None)
        node_counter = 0  
        fringe = [(self.priority(root_node), node_counter, root_node)]

        while fringe:
            _, _, current_node = heappop(fringe)

            successors = self.get_successors(current_node.state)

            for successor_state in successors:
                if any(np.array_equal(successor_state, visited) for visited in self.visited):
                    continue

                self.visited.append(successor_state)
                new_cost = current_node.cost_from_start + 1
                successor_node = Node(successor_state, new_cost, current_node)

                if self.goal_test(successor_state):
                    self.draw(successor_node)
                    return

                node_counter += 1  
                heappush(fringe, (self.priority(successor_node), node_counter, successor_node))


    


if __name__ == "__main__":
    
    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
    start_arrays = [np.array([[1,2,0],[3,4,6],[7,5,8]]),
                    np.array([[8,1,3],[4,0,2],[7,6,5]])]
    methods = ["Hamming", "Manhattan"]
    algorithms = ['Depth-Limited-DFS', 'BFS', 'Greedy', 'AStar']
    
    parser = argparse.ArgumentParser(description='eight puzzle')

    parser.add_argument('-array', dest='array_index', required = True, type = int, help='index of array')
    parser.add_argument('-method', dest='method_index', required = True, type = int, help='index of method')
    parser.add_argument('-algorithm', dest='algorithm_index', required = True, type = int, help='index of algorithm')

    args = parser.parse_args()

    # Example:
    # Run this in the terminal using array 0, method Hamming, algorithm AStar:
    #     python eight_puzzle.py -array 0 -method 0 -algorithm 3
    game = EightPuzzle(start_arrays[args.array_index], goal, methods[args.method_index], algorithms[args.algorithm_index], args.array_index)
    game.solve()
