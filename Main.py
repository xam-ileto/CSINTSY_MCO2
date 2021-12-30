from Game import Game

game = Game()
game_over = False

while game.current_board.check_game_over(game.player_turn) == False:
    game.current_board.print_board()
    game.simulate_turn(game.player_turn)
    game.change_turn()
    # print("BOARD AFTER MOVE")
    # game.current_board.print_board()

print("Game over!")