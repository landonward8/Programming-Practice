from itertools import permutations
import math
import argparse
from draw import draw_path
from test import test_path

class password():
    def __init__(self, rule):
        self.rule = rule
        # Longest distance
        self.longest_length = 0.0
        # List of longest path. The longest path is not unique. 
        self.longest_path = []
        # Your code goes here:
        self.coordinates = {'1': (0, 0), '2': (1, 0), '3': (2, 0), '4': (0, 1), 
        '5': (1, 1), '6': (2, 1), '7': (0, 2), '8': (1, 2), '9': (2, 2)}
        self.middle_point = [[['7','9'],'8'],[['4','6'],'5'],[['1','3'],'2'],[['7','1'],'4'],[['8','2'],'5'],[['9','3'],'6'],[['7','3'],'5'],[['9','1'],'5']]
    
    # Find the longest path
    def find_longest_path(self):
        # Your code goes here:
        perm = permutations('123456789')
        for path in perm:
            path = ''.join(path)
            is_path = False
            if self.rule == 1:
                for feasible_path in self.middle_point:  
                    if ''.join(feasible_path[0]) in path or ''.join(reversed(feasible_path[0])) in path:
                        is_path = True
                        break
            elif self.rule == 2:
                for feasible_path in self.middle_point:  
                    if ''.join(feasible_path[0]) in path:
                        index = path.index(''.join(feasible_path[0]))
                        partial_string = path[:index]
                        if feasible_path[1] not in partial_string:
                            is_path = True
                            break
            if is_path:
                continue
            length = 0 
            for i in range(1, len(path)):
                length += self.distance(self.coordinates[path[i-1]], self.coordinates[path[i]])
            if length > self.longest_length:
                self.longest_length = length
                self.longest_path = [path]
            elif length == self.longest_length:
                self.longest_path.append(path)

        
    # Calculate distance between two vertices
    # Format of a coordinate is a tuple (x_value, y_value), for example, (1,2), (0,1)
    def distance(self, vertex1, vertex2):
        return math.sqrt((vertex1[0]-vertex2[0])**2 + (vertex1[1]-vertex2[1])**2)

    # Print and save the result
    def print_result(self):
        print("The longest length using rule " + str(self.rule) + " is:")
        print(self.longest_length)
        print()
        print("All paths with longest length using rule " + str(self.rule) + " are:") 
        print(self.longest_path)
        print()
        with open('results_rule'+str(self.rule)+'.txt', 'w') as file_handler:
            file_handler.write("{}\n".format(self.longest_length)) 
            for path in self.longest_path:
                file_handler.write("{}\n".format(path)) 

    # test the result 
    def test(self):
        test_path(self.longest_length, self.longest_path, self.rule)

    # draw first result
    def draw(self):
        if len(self.longest_path) > 0:
            draw_path(self.longest_path[0], self.rule)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='PatternLock')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='Index of the rule')
    args = parser.parse_args()

    # usage
    # python PatternLock.py -rule 1
    # python PatternLock.py -rule 2
    
    # Initialize the object using rule 1 or rule 2
    run = password(args.rule)
    # Find the longest path
    run.find_longest_path()
    # Print and save the result
    run.print_result()
    run.test()
    # Draw the first longest path
    run.draw()
    # Verify the result 
    # run.verify()