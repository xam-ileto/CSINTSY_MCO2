from Game import Game

game = Game()

while game.current_board.check_game_over(game.player_turn) == False:
    game.current_board.print_board()
    game.simulate_turn(game.player_turn)
    game.change_turn()

print("Game over!")