from copy import deepcopy

class NodeUserMoves:
    def __init__(self, piece, board, row, col):
        self.moved_piece = deepcopy(piece)
        self.board_moves = []
        self.piece_moves = []

        # add starting move
        self.add_move(deepcopy(board), row, col)
    
    def get_final_board(self):
        return self.board_moves[-1]
    
    def add_move(self, board, row, col):
        self.board_moves.append(board)
        position = [row, col]
        self.piece_moves.append(position)
