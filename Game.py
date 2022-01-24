from copy import deepcopy
from Board import Board
from Tree import Tree
from AiNode import AiNode

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
        if self.player_turn == "Red":
            # show possible moves and ask player for move
            move = self.current_board.choose_move(self.current_board._next_user_moves(self.current_board.pieces_of_color(color)))
        else:
            # if white turn
            print("AI is calculating next move...")
            root = AiNode(self.current_board, 0, "Red", None)
            tree = Tree(root, 2)
            
            move = tree.minimax(root, 0, -10000, 10000, "White", False)
            visited = []
            tree.print_tree(visited, tree.root)
            print("Without move ordering: " + str(tree.no_ordering_counter))
            visited = []
            print('-----MOVE ORDERING---------')
            tree.move_ordering(visited, tree.root)
            move = tree.minimax(root, 0, -10000, 10000, "White", True)
            visited = []
            tree.print_tree(visited, tree.root)
            print("With move ordering: " + str(tree.ordering_counter))
            
            # visited = []
            # tree.print_tree(visited, tree.root)

        # perform the move and change the board
        self.current_board = deepcopy(move.board)
