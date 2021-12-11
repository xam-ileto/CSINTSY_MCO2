class Piece:
    def __init__(self, name, row, col, color):
        self.name = name
        self.row = row
        self.col = col
        self.color = color
        self.is_king = False
        pass

    def move(self, row, col):
        self.row = row
        self.col = col

    def make_king(self):
        self.name = self.name + "K"
        self.is_king = True