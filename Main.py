from Board import Board

b = Board("Start")
b.print_board()

b.pieces[0].make_king()
b.print_board()