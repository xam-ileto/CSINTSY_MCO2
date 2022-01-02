
from Board import Board
class AiNode:
    def __init__(self, board, depth, color):
        self.board = board
        self.depth = depth
        self.turn = color
        
        self.score = self.calculate_score()
        self.children = []
    
    def add_children(self):
        '''generates the next possible nodes given the current board'''
        for next_moves in self.board._next_user_moves(self.board.pieces_of_color(self.turn)):
            if self.turn == "White":
                next_color = "Red"
            else:
                next_color = "White"
            
            next_moves.board.calculate_stats()
            new_node = AiNode(next_moves.board, self.depth + 1, next_color)
            self.children.append(new_node)
    
    def calculate_score(self):
        '''calculates the score for the node'''
        return self.board.white_pieces - self.board.red_pieces + (self.board.white_kings * 0.5 - self.board.red_kings * 0.5)
    
    def sort_children():
        pass
    
    def print_node(self):
        '''prints node for debugging purposes'''
        tab = ' ' * self.depth
        
        print(tab + "Node score: " + str(self.score))
        print(tab + "turn: " + self.turn)
        self.board.print_board()
        