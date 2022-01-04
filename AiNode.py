
from Board import Board
class AiNode:
    def __init__(self, board, depth, color, moved_piece):
        self.board = board
        self.depth = depth
        self.turn = color
        self.moved_piece = moved_piece # is None if root node
        
        self.score = self.calculate_score()
        self.children = []
    
    def add_children(self):
        '''generates the next possible nodes given the current board'''
        if self.turn == "White":
            next_color = "Red"
        else:
            next_color = "White"
        for next_moves in self.board._next_user_moves(self.board.pieces_of_color(next_color)):
            
            next_moves.board.calculate_stats()
            new_node = AiNode(next_moves.board, self.depth + 1, next_color, next_moves.moved_piece)
            self.children.append(new_node)
    
    def calculate_score(self):
        '''calculates the score for the node'''
        outcome = 0
        white_pieces = self.board.white_pieces
        red_pieces = self.board.red_pieces
        
        for piece in self.board.pieces_of_color("White"):
            if piece.is_king:
                outcome += 8
            else:
                outcome += 5
            
            # if at edge, plus 7
            if piece.row == 0 or piece.col == 0 or piece.row == 7 or piece.col == 7:
                outcome += 7
            
            
            # if AI can be eaten, -3
            if piece.row + 1 > 7 or piece.row - 1 < 0 or piece.col + 1 > 7 or piece.col - 1 < 0:
                continue
            
            piece_check = self.board._piece_in_pos(piece.row + 1, piece.col - 1)
            if  piece_check != None: # if there is a piece in the position
                if piece_check.color == "Red" and self.board._piece_in_pos(piece.row - 1, piece.col + 1) == None: # check if the piece is an enemy and if partnering tile is empty
                    outcome -= 3
            
            piece_check = self.board._piece_in_pos(piece.row + 1, piece.col + 1)
            if  piece_check != None: # if there is a piece in the position
                if piece_check.color == "Red" and self.board._piece_in_pos(piece.row - 1, piece.col - 1) == None: # check if the piece is an enemy and if partnering tile is empty
                    outcome -= 3
            
            piece_check = self.board._piece_in_pos(piece.row - 1, piece.col - 1)
            if  piece_check != None: # if there is a piece in the position
                if piece_check.color == "Red" and piece_check.is_king and self.board._piece_in_pos(piece.row + 1, piece.col + 1) == None: # check if the piece is an enemy and if partnering tile is empty, check also if king
                    outcome -= 3
            
            piece_check = self.board._piece_in_pos(piece.row - 1, piece.col + 1)
            if  piece_check != None: # if there is a piece in the position
                if piece_check.color == "Red" and piece_check.is_king and self.board._piece_in_pos(piece.row + 1, piece.col - 1) == None: # check if the piece is an enemy and if partnering tile is empty, check also if king
                    outcome -= 3
            
            # if AI can eat, plus 6
            if piece.row + 2 > 7 or piece.row -2 < 0:
                continue
            
            piece_check = self.board._piece_in_pos(piece.row + 1, piece.col - 1)
            if  piece_check != None:
                if piece_check.color == "Red" and self.board._piece_in_pos(piece.row + 2, piece.col - 2) == None:
                    outcome += 6
            
            if piece.row + 2 > 7 or piece.col + 2 > 7:
                continue
                    
            piece_check = self.board._piece_in_pos(piece.row + 1, piece.col + 1)
            if  piece_check != None:
                if piece_check.color == "Red" and self.board._piece_in_pos(piece.row + 2, piece.col + 2) == None:
                    outcome += 6
        
        return outcome + (white_pieces - red_pieces) * 1000
    
    def sort_children_descending(self):
        '''Sorts the children of this node in descending order for move ordering'''
        self.children.sort(key = lambda x: x.score, reverse= True)
    
    def print_node(self):
        '''prints node for debugging purposes'''
        tab = ' ' * self.depth * 5
        
        print(tab + "Node score: " + str(self.score))
        print(tab + "Node depth: " + str(self.depth))
        print(tab + "turn: " + self.turn)
        self.board.print_board()
        