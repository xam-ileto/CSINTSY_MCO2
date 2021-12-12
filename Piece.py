class Piece:
    def __init__(self, name, row, col, color):
        self.name = name
        self.row = row
        self.col = col
        self.color = color
        self.is_king = False

    def move(self, row, col):
        self.row = row
        self.col = col

    def make_king(self):
        self.is_king = True

    def _is_enemy_piece(self, player_color):
        # pass string of current team color
        # checks if passed piece is enemy of current player
        if self.color != player_color:
            return True
        
        return False