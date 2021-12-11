from Piece import Piece
from collections import defaultdict

class Board:
    def __init__(self, *args):

        if isinstance(args[0], str):
            self._init_start()

        pass
    # if user passes true, then call _init_start
    # else (if user passes a board), set board to be this

    def _init_start(self):
        self.pieces = []

        # generate list of starting positions with pieces
        starting_positions = []
        for i in range(0, 8):
                if (i == 3) or (i == 4):
                    continue
                if (i % 2 == 0): #if number is odd
                    for x in range(1, 8, 2):
                        pos = [i,x]
                        starting_positions.append(pos)
                else: # if number is even
                    for x in range(0, 7, 2):
                        pos = [i,x]
                        starting_positions.append(pos)

        # generate each starting piece
        whitecount = 1
        redcount = 1
        for i in range(0, len(starting_positions)):
            row = starting_positions[i][0]
            col = starting_positions[i][1]
            if i < 12: # white piece
                name = "W" + str(whitecount)
                new_piece = Piece(name, row, col, "White")
                self.pieces.append(new_piece)
                whitecount += 1
            else: # red piece
                name = "R" + str(redcount)
                new_piece = Piece(name, row, col, "Red")
                self.pieces.append(new_piece)
                redcount += 1
        
        # set remaining piece values
        self.remaining_red = 12
        self.remaining_white = 12
        self.remaining_red_kings = 0
        self.remaining_white_kings = 0
            

    def _init_this():
        # might need to use deep copy
        pass

    def choose_move():
        # calls _next_user_moves
        pass
    
    def print_board(self):
        print("---BOARD---")
        for i in range(0, 8):
            if(i == 0):
                print("     0    1    2    3    4    5    6    7")
            print(str(i + 1) + "  ", end = "")
            for j in range(0, 8):
                print("|   |", end = "")
            print("")
        print("")
