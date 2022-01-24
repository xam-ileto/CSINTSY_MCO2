from Game import Game
# TO DO
from AiNode import AiNode

game = Game()

# show game instructions
print("Welcome to the game of checkers!")
print("\nHere are the mechanics:")
print("1. You (the player) are playing for color red, while the AI is playing for color white")
print("2. The board is represented below, with the names of the pieces written in a specific format. The letter symbolizes the color (R= Red, W= White)")
print("3. Once a piece reaches the end of the board, a K will be appended to its name, signifying that it is a king piece")
print("4. As per the rules of the standard checkers game, all jumps are forced")
print("\nGood luck!\n")

while game.current_board.check_game_over(game.player_turn) == False:
    game.current_board.print_board()
    
    game.simulate_turn(game.player_turn)
    game.change_turn()

# game over
if (game.player_turn == "White"):
    print("Red wins!")
else:
    print("White wins!")