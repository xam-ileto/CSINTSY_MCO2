
from Board import Board
class AiNode:
    def __init__(self, board, depth, color, moved_piece):
        self.board = board
        self.depth = depth
        self.turn = color
        self.moved_piece = moved_piece # is None if root node
        
        self.score = self.board.calculate_score()
        self.children = []
    
    def add_children(self):
        '''generates the next possible nodes given the current board'''
        if self.turn == "White":
            next_color = "Red"
        else:
            next_color = "White"
        for next_moves in self.board._next_user_moves(self.board.pieces_of_color(self.turn)):
            
            next_moves.board.calculate_stats()
            new_node = AiNode(next_moves.board, self.depth + 1, next_color, next_moves.moved_piece)
            self.children.append(new_node)
    
    def sort_children_descending(self):
        '''Sorts the children of this node in descending order for move ordering'''
        self.children.sort(key = lambda x: x.score, reverse= True)
    
    def print_node(self):
        '''prints node for debugging purposes'''
        tab = ' ' * self.depth * 5
        
        print(tab + "Node score: " + str(self.score))
        print(tab + "Node depth: " + str(self.depth))
        print(tab + "turn: " + self.turn)
        # self.board.print_board()
        