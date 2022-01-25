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
            no_ordering_tree = Tree(root, 4)
            move = no_ordering_tree.minimax(root, 0, -10000, 10000, "White", False)
            visited = []
            no_ordering_tree.count_nodes(visited,no_ordering_tree.root)
            print("nodes generated: " + str(no_ordering_tree.number_of_nodes))
            print("Without move ordering: " + str(no_ordering_tree.counter))
            visited = []
            no_ordering_tree.print_tree(visited, no_ordering_tree.root)
            
            
            print('-----MOVE ORDERING---------')
            root = AiNode(self.current_board, 0, "Red", None)
            ordering_tree = Tree(root, 4)
            move = ordering_tree.minimax(root, 0, -10000, 10000, "White", True)
            visited = []
            ordering_tree.print_tree(visited,ordering_tree.root)
            visited = []
            ordering_tree.count_nodes(visited,ordering_tree.root)
            print("nodes generated: " + str(ordering_tree.number_of_nodes))
            print("With move ordering: " + str(ordering_tree.counter))

        # perform the move and change the board
        self.current_board = deepcopy(move.board)
