from Board import Board

class Game:
    def __init__(self):
        self.current_board = Board("Start")
        self.player_turn = "Red"
    
    def change_turn(self):
        '''Changes turn to either red or white'''
        if self.player_turn == "Red":
            self.player_turn = "White"
        else:
            self.player_turn = "Red"
    
    def simulate_turn(self, color):
        # show possible moves and ask player for move
        move = self.current_board.choose_move(self.current_board._next_user_moves(self.current_board.pieces_of_color(color)))

        # perform the move and change the board
        self.current_board = move.board
