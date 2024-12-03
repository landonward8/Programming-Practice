from copy import deepcopy as copy
import argparse
from animation import draw
# landon ward

class Node():
    def __init__(self, board, jumpfrom = None, jumpover = None, jumpto = None):
        self.board = board
        self.jumpfrom = jumpfrom
        self.jumpover = jumpover
        self.jumpto = jumpto

class peg:
    def __init__(self, start_row, start_col, rule):
        self.size = 5
        self.start_row, self.start_col, self.rule = start_row, start_col, rule
        # board
        # initilize board
        self.board = [[1 for j in range(i+1)] for i in range(self.size)]
        self.board[start_row][start_col] = 0
        self.start = Node(copy(self.board))
        # path
        self.path = [self.start]
        self.directions = [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, 2)]
        
        
        
       #  self.path = self.path.append(Node(copy(self.board)))
        # Do some initialization work here if you need:
        

    def draw(self):
        if self.success():
            draw(self.path, self.start_row, self.start_col, self.rule)
        else:
            print("No solution were found!")


    def success(self):
        # your code goes here:
        # calculate the sum of self.board 
        # if the sum is 1, return True
        total = sum(sum(row) for row in self.board)

        if self.rule == 1:
            return total == 1 and self.board[self.start_row][self.start_col] == 1

        return total == 1

        
    def solve(self):

    #     def solve():

    # if board is solution:
    #     return True

    # for one available jump:
    
    #     process board and path

    #     if solve():
    #         return True 

    #     backtrack board and path   

    # return False

        if self.success():
            return True

        for jumpfrom, jumpover, jumpto in self.get_valid_jumps():
            self.make_jump(jumpfrom, jumpover, jumpto)
            self.path.append(Node(copy(self.board), jumpfrom, jumpover, jumpto))

            if self.solve():
                return True

            self.path.pop()
            self.undo_jump(jumpfrom, jumpover, jumpto)

        return False
    

    def get_valid_jumps(self):
        valid_jumps = []
        for row in range(self.size):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 1: # only positions with a peg
                    for r, c in self.directions: # check all directions
                        jumpover = (row + r // 2, col + c // 2)
                        jumpto = (row + r, col + c)
                        # add to valid jump
                        if self.is_valid_jump((row, col), jumpover, jumpto):
                            valid_jumps.append(((row, col), jumpover, jumpto))
        return valid_jumps

        
    def is_valid_jump(self, jumpfrom, jumpover, jumpto):
        r1, c1 = jumpfrom
        r2, c2 = jumpover
        r3, c3 = jumpto
        # jump in bounds 
        if not (0 <= r3 < self.size and 0 <= c3 <= r3):
            return False
        if not (0 <= r2 < self.size and 0 <= c2 <= r2):
            return False

        return (
            self.board[r1][c1] == 1 and  
            self.board[r2][c2] == 1 and  
            self.board[r3][c3] == 0     
        )
    
    def make_jump(self, jumpfrom, jumpover, jumpto):
            r1, c1 = jumpfrom
            r2, c2 = jumpover
            r3, c3 = jumpto

            self.board[r1][c1] = 0  # place and remove pegs
            self.board[r2][c2] = 0  
            self.board[r3][c3] = 1  

    def undo_jump(self, jumpfrom, jumpover, jumpto):
            r1, c1 = jumpfrom
            r2, c2 = jumpover
            r3, c3 = jumpto

            self.board[r1][c1] = 1  
            self.board[r2][c2] = 1  
            self.board[r3][c3] = 0  
        
                
                    
        
    

        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='peg game')

    parser.add_argument('-hole', dest='position', required = True, nargs = '+', type = int, help='initial position of the hole')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='index of rule')

    args = parser.parse_args()

    start_row, start_col = args.position
    if start_row > 4:
        print("row must be less or equal than 4")
        exit()
    if start_col > start_row:
        print("column must be less or equal than row")
        exit()

    # Example: 
    # python peg.py -hole 0 0 -rule 0
    game = peg(start_row, start_col, args.rule)
    game.solve()
    game.draw()
    