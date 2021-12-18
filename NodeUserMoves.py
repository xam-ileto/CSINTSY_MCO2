from copy import deepcopy

class NodeUserMoves:
    def __init__(self, piece, board, row, col):
        # moved_piece is the name of the passed piece
        self.moved_piece = piece
        self.board_moves = []
        self.piece_moves = []

        # add starting move
        self.add_move(deepcopy(board), row, col)
    
    def get_final_board(self):
        return self.board_moves[-1]
    
    def get_final_move(self):
        return self.piece_moves[-1]
    
    def add_move(self, board, row, col):
        self.board_moves.append(board)
        position = [row, col]
        self.piece_moves.append(position)
    
    def print_node(self):
        print("node: " + self.moved_piece)

        for moves in self.piece_moves:
            print("[" + str(moves[0]) + "," + str(moves[1]) + "],  ", end ='')
        print("")
