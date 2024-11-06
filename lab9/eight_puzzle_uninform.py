import numpy as np
from animation import draw
import argparse

# landon ward

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

    def __init__(self, start_state, goal_state, algorithm, array_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.visited = []  # state
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
        draw(path[::-1], self.array_index, self.algorithm)

    # solve it
    def solve(self):
        fringe = []  # node
        state = self.start_state.copy()  # use copy() to copy value instead of reference

        if self.goal_test(state):
            return state

        node = Node(state, 0, None)
        self.visited.append(state)
        fringe.append(node)

        max_depth = 15

        while fringe:
            if self.algorithm == 'Depth-Limited-DFS':  # stack
                node = fringe.pop(0)

                if node.cost_from_start > max_depth:
                    continue

            elif self.algorithm == 'BFS':  # queue
                node = fringe.pop()

            print(node.state)
            print()

            successors = self.get_successors(node.state)
            print(successors)
            print()

            for next_state in successors:
                seen = False
                for visited in self.visited:
                    if np.array_equal(next_state, visited):
                        seen = True
                        break

                if seen:
                    continue

                self.visited.append(next_state)

                next_cost = node.cost_from_start + self.get_cost(next_state, node.state)
                next_node = Node(next_state, next_cost, node)

                if self.goal_test(next_state):
                    self.draw(next_node)
                    return

                if self.algorithm == 'Depth-Limited-DFS':
                    fringe.append(next_node)
                elif self.algorithm == 'BFS':
                    fringe.insert(0, next_node)

            print(self.visited)

            for o in fringe:
                print(o.state)


if __name__ == "__main__":
    goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    start_arrays = [np.array([[0, 1, 3], [4, 2, 5], [7, 8, 6]]),  # easy one. use this in lab
                    np.array([[0, 2, 3], [1, 4, 6], [7, 5, 8]])]  # medium one.

    algorithms = ['Depth-Limited-DFS', 'BFS']

    parser = argparse.ArgumentParser(description='eight puzzle')

    parser.add_argument('-array', dest='array_index', required=True, type=int, help='index of array')
    parser.add_argument('-algorithm', dest='algorithm_index', required=True, type=int, help='index of algorithm')

    args = parser.parse_args()

    # run this in the terminal using array 0, algorithm BFS
    # python eight_puzzle_uninform.py -array 0 -algorithm 1
    game = EightPuzzle(start_arrays[args.array_index], goal, algorithms[args.algorithm_index], args.array_index)
    game.solve()
