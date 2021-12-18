from copy import deepcopy
from typing import Text
from Board import Board

b = Board("Start")

# positions R3 so it can jump
b.get_piece("R3").move(3,4)
b.get_piece("R2").move(3,2)
b.get_piece("R1").move(5,2)
b._eat_piece(b.get_piece("R6"))

b.print_board()


b._next_user_moves(b.pieces_of_color("White"))