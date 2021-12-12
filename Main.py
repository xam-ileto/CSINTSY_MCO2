from Board import Board

b = Board("Start")

b.get_piece("W1").make_king()

b.get_piece("W1").move(4,3)
b.get_piece("R2").move(3,0)
b.get_piece("R3").move(4,0)
b.get_piece("R5").move(5,2)
b.get_piece("W11").move(3,4)
b.print_board()

print("possible moves for W1")
print(b.next_piece_moves(b.get_piece("W1")))

