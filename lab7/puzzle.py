import argparse
import draw
# landon ward
# completed with Kelii outside of class

# class of board
# every board is an object of the class Board 
class Board:
    def __init__(self, left, right, bottom, top):
        self.left, self.right, self.bottom, self.top = left, right, bottom, top
    
    # call this method to return four boundaries of the board 
    def get_boundary(self):
        return self.left, self.right, self.bottom, self.top

class Puzzle:
    def __init__(self, size, block):
        # size is the size of board. 
        # block is the position (x,y) of the block 
        
        # fill the initial block as black
        draw.draw_one_square(block, 'k')
        # draw the grid on the board 
        draw.grid(size)

        # create the board at full size 
        board = Board(1, size, 1, size) 
        # call solve to fill the Tromino recursively using divide and conquer 
        self.solve(block, board)
        
        # show and save the result in a picture 
        draw.save_and_show(size, block)

    blockQuad = 0

    def solve(self, block, board):
        # block is a position (row, column) and board is an object of Board class 
        # recursively call solve() on four small size boards with only one block on each board
        # stop the recursive call when reaching to the base case, which is board 2*2
        #  
        # call draw.draw_one_tromino(type, board) to draw one type of tromino at the center of the board. The type of the tromino is an integer 1 to 4 as explained in the instruction and the board is an object of Board class where you want to draw the tromino at its center. 

        left, right, bottom, top = board.get_boundary()
        # your code goes here:

        block_x, block_y = block
        
        

        if right - left <= 2 and top - bottom <= 2:
            type = self.get_tromino_type(block, board)
            draw.draw_one_tromino(type, board)
            return

        x_middle = (right + left)//2
        y_middle = (top + bottom)//2
        quad1 = Board(x_middle, right, y_middle, top)
        quad2 = Board(left, x_middle, y_middle, top)
        quad3 = Board(left, x_middle, bottom, y_middle)
        quad4 = Board(x_middle, right, bottom, y_middle)
        quad5 = Board(x_middle - 1, x_middle + 1, y_middle - 1, y_middle + 1)

    

        if block_x > x_middle and block_y > y_middle:
            draw.draw_one_tromino(1, quad5)
            self.solve(block, quad1)  
            self.solve((x_middle, y_middle + 1), quad2)  
            self.solve((x_middle, y_middle), quad3)  
            self.solve((x_middle + 1, y_middle), quad4)  

        elif block_x <= x_middle and block_y > y_middle:
            
            draw.draw_one_tromino(2, quad5)
            self.solve(block, quad2)
            self.solve((x_middle + 1, y_middle + 1), quad1)
            self.solve((x_middle, y_middle), quad3)
            self.solve((x_middle + 1, y_middle), quad4)

        elif block_x <= x_middle and block_y <= y_middle:
            
            draw.draw_one_tromino(3, quad5)
            self.solve(block, quad3)
            self.solve((x_middle + 1, y_middle + 1), quad1)
            self.solve((x_middle, y_middle + 1), quad2)
            self.solve((x_middle + 1, y_middle), quad4)

        elif block_x > x_middle and block_y <= y_middle:
            draw.draw_one_tromino(4, quad5)
            self.solve(block, quad4)
            self.solve((x_middle + 1, y_middle + 1), quad1)
            self.solve((x_middle, y_middle + 1), quad2)
            self.solve((x_middle, y_middle), quad3)

    def get_tromino_type(self, block, board):
        # return the type of the tromino you should draw based on the position of the block and the board.
        left, right, bottom, top = board.get_boundary() 
        # your code goes here:

        x_middle = (right + left) // 2
        y_middle = (top + bottom) // 2
        block_x, block_y = block

        if block_x > x_middle and block_y > y_middle:
            return 1
        elif block_x == x_middle and block_y > y_middle:
            return 2
        elif block_x == x_middle and block_y == y_middle:
            return 3
        elif block_x > x_middle and block_y == y_middle:
            return 4




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='puzzle')

    parser.add_argument('-size', dest='size', required = True, type = int, help='size of the board: 2^n')
    parser.add_argument('-block', dest='block', required = True, nargs='+', type = int, help='position of the initial block')

    args = parser.parse_args()

    # size must be a positive integer 2^n
    # block must be two integers between 1 and size 
    game = Puzzle(args.size, tuple(args.block))

    # game = puzzle(8, (1,1))
    # python puzzle.py -size 8 -block 1 1