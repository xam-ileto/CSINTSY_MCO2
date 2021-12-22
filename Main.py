from copy import deepcopy
from typing import Text
from Board import Board

b = Board("Start")

# positions R3 so it can jump
b.get_piece("R3").move(0,0)
print(b.get_piece("R3").is_king)
b.get_piece("W1").move(7,7)
print(b.get_piece("W1").is_king)

