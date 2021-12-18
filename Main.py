from copy import deepcopy
from typing import Text
from Board import Board

b = Board("Start")

# positions R3 so it can jump
b.get_piece("R3").move(4,4)
b.get_piece("W11").move(3,5)
b.get_piece("W3").move(1,5)

b.print_board()

b._next_user_moves(b.pieces_of_color("Red"))