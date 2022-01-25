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
            tree = Tree(root, 4)
            
            move = tree.minimax(root, 0, -10000, 10000, "White")
            visited = []
            # tree.print_tree(visited, tree.root)
            
            visited = []
            print('-----MOVE ORDERING---------')
            tree.move_ordering(visited, tree.root)
            move = tree.minimax(root, 0, -10000, 10000, "White")
            visited = []
            tree.print_tree(visited, tree.root)
            print("Without move ordering: " + str(tree.no_ordering_counter))
            print("With move ordering: " + str(tree.ordering_counter))
            visited = []
            tree.count_nodes(visited, tree.root)
            print("num of nodes: " + str(tree.number_of_nodes))
            
            # tree.root.board.print_board()
            # tree.root.children[0].board.print_board()
            # tree.root.children[0].children[0].board.print_board()
            # tree.root.children[0].children[0].children[0].board.print_board()
            # tree.root.children[0].children[0].children[0].children[0].board.print_board()
            
            # visited = []
            # tree.print_tree(visited, tree.root)

        # perform the move and change the board
        self.current_board = deepcopy(move.board)
