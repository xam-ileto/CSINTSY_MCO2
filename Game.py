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
            move = self.current_board.choose_move(self.current_board._next_user_moves(self.current_board.pieces_of_color(color)))
        else:
            # if white turn
            print("AI is calculating next move...")
            
            root = AiNode(self.current_board, 0, "White")
            ordering_tree = Tree(root, 2)
            move, score = ordering_tree.minimax(ordering_tree.root, 2, -100000, 100000, True, True)

        # perform the move and change the board
        self.current_board = deepcopy(move.board)
