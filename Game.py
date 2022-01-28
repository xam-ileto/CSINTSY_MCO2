from copy import deepcopy
from Board import Board
from Tree import Tree
from AiNode import AiNode

class Game:
    def __init__(self):
        self.current_board = Board("Start")
        self.player_turn = "Red"
    
    def game(self):
        # show game instructions
        print("Welcome to the game of checkers!")
        print("\nHere are the mechanics:")
        print("1. You (the player) are playing for color red, while the AI is playing for color white")
        print("2. The board is represented below, with the names of the pieces written in a specific format. The letter symbolizes the color (R= Red, W= White)")
        print("3. Once a piece reaches the end of the board, a K will be appended to its name, signifying that it is a king piece")
        print("4. As per the rules of the standard checkers game, all jumps are forced")
        print("\nGood luck!\n")

        while self.current_board.check_game_over(self.player_turn) == False:
            self.current_board.print_board()
            
            self.simulate_turn(self.player_turn)
            self.change_turn()

        # game over
        self.current_board.print_board()
        if (self.player_turn == "White"):
            print("Red wins!")
        else:
            print("White wins!")
    
    def change_turn(self):
        '''Changes turn to either red or white'''
        if self.player_turn == "Red":
            self.player_turn = "White"
        else:
            self.player_turn = "Red"
    
    def simulate_turn(self, color):
        if self.player_turn == "Red":
            # show possible moves and ask player for move
            move = self.current_board.choose_move(self.current_board.next_user_moves(self.current_board.pieces_of_color(color)))
        else:
            # if white turn
            print("AI is calculating next move...")
            
            root = AiNode(self.current_board, 0, "White")
            ordering_tree = Tree(root, 2)
            move, score = ordering_tree.minimax(ordering_tree.root, 2, -100000, 100000, True, True)
            
            # TO DO
            # With move ordering
            DEPTH = 2
            print("WITH MOVE ORDERING")
            visited = []
            ordering_tree.print_tree(visited, ordering_tree.root)

            print("nodes explored: " + str(ordering_tree.counter))
            visited = []
            ordering_tree.count_nodes(visited, ordering_tree.root)
            print("total nodes: " + str(ordering_tree.number_of_nodes))

            # Without move ordering
            print("WITHOUT MOVE ORDERING")
            new_root = AiNode(self.current_board, 0, "White")
            new_tree = Tree(new_root, DEPTH)
            move, move_score = new_tree.minimax(new_tree.root,DEPTH,-100000,100000,True,False)

            visited = []
            new_tree.print_tree(visited,new_tree.root)

            print("nodes explored: " + str(new_tree.counter))
            visited = []
            new_tree.count_nodes(visited, new_tree.root)
            print("total nodes: " + str(new_tree.number_of_nodes))

            # No pruning, with ordering
            print("NO PRUNING, WITH ORDERING")
            root3 = AiNode(self.current_board, 0, "White")
            tree3 = Tree(root, DEPTH)
            move, move_score = tree3.minimax_no_pruning(tree3.root, DEPTH, True, True)

            visited = []
            tree3.count_nodes(visited, tree3.root)

            # visited = []
            # tree3.print_tree(visited, tree3.root)
            print("total nodes: " + str(tree3.number_of_nodes))

            # No pruning, without ordering
            print("NO PRUNING, WITHOUT ORDERING")
            root4 = AiNode(self.current_board, 0, "White")
            tree4 = Tree(root, DEPTH)
            move, move_score = tree4.minimax_no_pruning(tree4.root, DEPTH, True, True)

            # visited = []
            # tree4.print_tree(visited, tree4.root)

            visited = []
            tree4.count_nodes(visited, tree4.root)
            print("total nodes: " + str(tree4.number_of_nodes))

        # perform the move and change the board
        self.current_board = deepcopy(move.board)
