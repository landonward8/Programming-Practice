import random 
from draw import draw
import argparse

# landon ward

class coin_robot:

    def __init__(self, row, column):
        random.seed(0)
        self.row = row
        self.column = column 
        # Get map
        self.map = [[0 for i in range(column)] for j in range(row)]
        self.generate_map()
        
    def generate_map(self):
        for i in range(self.row):
            for j in range(self.column):
                if random.random() > 0.7:
                    self.map[i][j] = 1 # coin
                else:
                    self.map[i][j] = 0

    def solve(self):
        # Your code goes here:
        # table for the max amount of coins
        max_coins = [[0 for _ in range(self.column)] for _ in range(self.row)]
        path = {}  

        for row in range(self.row):  
            for col in range(self.column):
                if row == 0 and col == 0:  
                    max_coins[row][col] = self.map[row][col]
                elif row == 0:
                    # add value to the left
                    max_coins[row][col] = max_coins[row][col - 1] + self.map[row][col]
                    path[(row, col)] = (row, col - 1)
                elif col == 0:  
                    # first colnum case
                    max_coins[row][col] = max_coins[row - 1][col] + self.map[row][col]
                    path[(row, col)] = (row - 1, col)
                else:  
                    if max_coins[row - 1][col] > max_coins[row][col - 1]:  
                        max_coins[row][col] = max_coins[row - 1][col] + self.map[row][col]
                        path[(row, col)] = (row - 1, col)
                    else:  
                        max_coins[row][col] = max_coins[row][col - 1] + self.map[row][col]
                        path[(row, col)] = (row, col - 1)

        backtrack_path = []
        current = (self.row - 1, self.column - 1) 
        while current in path:
            backtrack_path.append(current) # add to the path
            current = path[current]
        backtrack_path.append((0, 0))
        backtrack_path.reverse()  

        total_coins = max_coins[self.row - 1][self.column - 1]

        # Modify this line to call draw() to draw the path 
        self.draw(total_coins, backtrack_path)

        

    # F is the max number of coin 
    # path is the route of the robot from top-left to bottom-right
    def draw(self, F, path):
        title = "row_"+str(self.row)+"_column_"+str(self.column)+"_value_"+str(F)
        draw(self.map, path, title)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='coin robot')

    parser.add_argument('-row', dest='row', required = True, type = int, help='number of row')
    parser.add_argument('-column', dest='column', required = True, type = int, help='number of column')

    args = parser.parse_args()

    # Example: 
    # python coin_robot.py -row 20 -column 20
    game = coin_robot(args.row, args.column)
    game.solve()