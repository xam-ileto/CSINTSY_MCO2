class NodeUserMoves:
    def __init__(self, piece):
        self.moved_piece = piece
        self.board_moves = []
        self.piece_moves = []
    
    def get_final_board(self):
        return self.board_moves[-1]
    
    def add_move(self, board, row, col):
        self.board_moves.append(board)
        position = [row, col]
        self.piece_moves.append(position)
