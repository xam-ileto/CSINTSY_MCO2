from typing import final
from Piece import Piece
from collections import deque
from NodeUserMoves import NodeUserMoves
from copy import deepcopy

class Board:
    def __init__(self, *args):
        # if user passes a string, then call _init_start
        if isinstance(args[0], str):
            self._init_start()
        # else (if user passes a board), set board to be this
        else:
            self._init_this(args[0])
    

    def _init_start(self):
        self.red_pieces = 12
        self.white_pieces = 12
        self.red_kings = self.white_kings = 0
        
        self.pieces = []

        # generate list of starting positions with pieces
        starting_positions = []
        for i in range(0, 8):
                if (i == 3) or (i == 4):
                    continue
                if (i % 2 == 0): #if number is odd
                    for x in range(1, 8, 2):
                        pos = [i,x]
                        starting_positions.append(pos)
                else: # if number is even
                    for x in range(0, 7, 2):
                        pos = [i,x]
                        starting_positions.append(pos)

        # generate each starting piece
        whitecount = 1
        redcount = 1
        for i in range(0, len(starting_positions)):
            row = starting_positions[i][0]
            col = starting_positions[i][1]
            if i < 12: # white piece
                name = "W" + str(whitecount)
                new_piece = Piece(name, row, col, "White")
                self.pieces.append(new_piece)
                whitecount += 1
            else: # red piece
                name = "R" + str(redcount)
                new_piece = Piece(name, row, col, "Red")
                self.pieces.append(new_piece)
                redcount += 1
            

    def _init_this(self, board):
        # copies passed board into self
        self.red_pieces = deepcopy(board.red_pieces)
        self.white_pieces = deepcopy(board.white_pieces)
        self.pieces = deepcopy(board.pieces)

    def pieces_of_color(self, color):
        # returns pieces of specific color
        # pass "White" or "Red"
        pieces = []
        for piece in self.pieces:
            if piece.color == color:
                pieces.append(piece)
        
        return pieces

    def next_piece_moves(self, piece):
        # shows the next possible immediate moves for a chosen piece
        # calls is_tile_valid

        possible_moves = []
        row = piece.row
        col = piece.col
        player_color = piece.color

        possible_tiles = {}
        if piece.is_king:
            # if piece is king, check 4 diagonal tiles
            # if the diagonal tile has a piece, check the diagonal of the tile
            # upper left tile
            possible_tiles["UL"] = self.get_diagonal("UL", row, col)
            # upper right
            possible_tiles["UR"] = self.get_diagonal("UR", row, col)
            # lower left
            possible_tiles["LL"] = self.get_diagonal("LL", row, col)
            # lower right
            possible_tiles["LR"] = self.get_diagonal("LR", row, col)
        else: # piece is not a king
            if player_color == "White":
                # lower left
                possible_tiles["LL"] = self.get_diagonal("LL", row, col)
                # lower right
                possible_tiles["LR"] = self.get_diagonal("LR", row, col)
            else: # player_color == "Red"
                # upper left tile
                possible_tiles["UL"] = self.get_diagonal("UL", row, col)
                # upper right
                possible_tiles["UR"] = self.get_diagonal("UR", row, col)
        
        for position, coordinate in possible_tiles.items():
            # if position is not valid, continue (no need to check)
            coordinate_row = coordinate[0]
            coordinate_col = coordinate[1]
            if self.is_tile_valid(coordinate_row, coordinate_col) == False:
                continue

            # if no piece in tile, add to possible moves
            piece_in_diagonal = self.piece_in_pos(coordinate_row, coordinate_col)
            if  piece_in_diagonal == None:
                possible_moves.append(coordinate)
            
            # else if there is a piece of opposite color, check diagonal tile
            # if no piece in diagonal tile, add to possible moves
            elif piece_in_diagonal.is_enemy_piece(player_color):
                if position == "UL":
                    skip_coordinates = self.get_diagonal("UL", coordinate_row, coordinate_col)
                elif position == "UR":
                    skip_coordinates = self.get_diagonal("UR", coordinate_row, coordinate_col)
                elif position == "LL":
                    skip_coordinates = self.get_diagonal("LL", coordinate_row, coordinate_col)
                elif position == "LR":
                    skip_coordinates = self.get_diagonal("LR", coordinate_row, coordinate_col)

                # if skip_coordinates is not valid, continue
                if self.is_tile_valid(skip_coordinates[0], skip_coordinates[1]) == False:
                    continue

                if self.piece_in_pos(skip_coordinates[0], skip_coordinates[1]) == None:
                    possible_moves.append(skip_coordinates)
                
        
        # return the list of possible moves
        return possible_moves
        

    def is_tile_valid(self, row, col):
        # checks if a passed position goes out of bounds
        if row < 0 or row > 7 or col < 0 or col > 7:
            # return false if out of bounds
            return False
        
        # return true if within bounds
        return True
    
    def eat_piece(self, piece):
        self.pieces.remove(piece)

    def piece_in_pos(self, row, col):
        for piece in self.pieces:
            if piece.col == col and piece.row == row:
                return piece
        
        return None

    def get_piece(self, name):
        # this does not take into account if the piece is a king
        for piece in self.pieces:
            if piece.name == name:
                return piece

    def get_diagonal(self, diagonal, row, col):
        # diagonal is a code for what diagonal to get
        # UL = upper left, UR = upper right, LL = lower left, LR = lower right
        # returns list with positions

        if diagonal == "UL":
            return [row - 1, col - 1]
        elif diagonal == "UR":
            return [row - 1, col + 1]
        elif diagonal == "LL":
            return [row + 1, col - 1]
        elif diagonal == "LR":
            return [row + 1, col + 1]

    def next_user_moves(self, player_pieces):
        # returns final possible moves for the player
        final_possible_moves = []
        movable_pieces = []

        # check which pieces can possibly move
        for piece in player_pieces:
            if self.next_piece_moves(piece) != []:
                movable_pieces.append(piece)

    
        # find moves for movable pieces
        for piece in movable_pieces:
            root_row = piece.row
            root_col = piece.col
            
            stack = deque() 

            for move in self.next_piece_moves(piece):
                # create node and starting board
                start_node = NodeUserMoves(piece.name, self, root_row, root_col)

                # if a skip, add to the stack
                if start_node.get_final_board().check_is_skip(start_node.get_final_board().get_piece(start_node.moved_piece), move[0]):
                    stack.append(start_node)
                else:
                    final_possible_moves.append(start_node)
                # add next move to the node
                

                new_board = Board(self)

                new_board.simulate_move(new_board.get_piece(piece.name), move[0], move[1])
                
                start_node.add_move(new_board, move[0], move[1])
            
            
            while(len(stack) != 0): # while there are still explorable nodes, keep exploring
                current_node = stack.popleft()
                current_board = current_node.get_final_board()
                current_piece = current_board.get_piece(piece.name)
                current_row = current_node.get_final_move()[0]
                current_col = current_node.get_final_move()[1]

                # check next possible moves if any of them skip
                unfiltered_next_possible_moves = current_board.next_piece_moves(current_piece)
                next_possible_moves = []
                for move in unfiltered_next_possible_moves:
                    skipCheck = self.check_is_skip(current_piece, move[0])
                    if skipCheck == True:
                        next_possible_moves.append(move)
                # results in next_possible_moves containing the possible moves for this current node

                has_no_moves = len(next_possible_moves) == 0
                # if next_piece_moves is empty 
                # add to final_possible_moves
                if (has_no_moves):
                    final_possible_moves.append(current_node)

                # else, create nodes for next possible moves and add to stack
                else:
                    for move in next_possible_moves:
                        new_node = deepcopy(current_node)
                        new_board = Board(current_board)
                        new_board.simulate_move(new_board.get_piece(piece.name), move[0], move[1])
                        new_node.add_move(new_board, move[0], move[1])
                        stack.appendleft(new_node)
        
        # find the longest possible move
        move_lengths = [len(node.piece_moves) for node in final_possible_moves]
        
        # if there are no possible moves, return an empty list
        if len(move_lengths) == 0:
            return []
        
        max_length = max(list(move_lengths))
        
        # remove moves less than the maximum
        final_possible_moves = [move for move in final_possible_moves if len(move.piece_moves) >= max_length]

        # if max length is 2 and there is at least one skip and one normal move, only keep skips
        if max_length == 2:
            skip_count = 0
            normal_count = 0

            for move in final_possible_moves:
                if move.is_last_move_skip:
                    skip_count += 1
                else:
                    normal_count += 1

            if skip_count > 0 and normal_count > 0:
                final_possible_moves = [move for move in final_possible_moves if move.is_last_move_skip]

        return final_possible_moves

                 
        
    def get_inner_diagonal(self, position, row, col):
        # pass position of tile (ex. "UR"/"UL")
        if position == "UL":
            row = row - 1
            col = col - 1
        elif position == "UR":
            row = row - 1
            col = col + 1
        elif position == "LL":
            row = row + 1
            col = col - 1
        else: # position == "UR"
            row = row + 1
            col = col + 1

        # returns immediate inner tile in that position
        return row, col
    
    def check_is_skip(self, piece, row):
        if (row  == piece.row - 2 or row == piece.row + 2):
            return True
        
        # else
        return False
    
    
    def check_which_diagonal(self, piece, row, col):
        current_row = piece.row
        current_col = piece.col

        # returns string of position of tile (ex. "UR"/"UL")
        # this is regardless if inner or outer position
        if (row < current_row and col < current_col):
            return "UL"
        elif (row < current_row  and col > current_col):
            return "UR"
        elif (row > current_row and col < current_col ):
            return "LL"
        else:
            return "LR"
    
    def simulate_move(self, piece, row, col):
        # function moves selected piece and also eats enemy if piece skips a tile when moving to row and col
        current_row = piece.row
        current_col = piece.col
        is_skip = self.check_is_skip(piece, row)

        moving_to_position = self.check_which_diagonal(piece, row, col)

        if (is_skip):
            # eat enemy
            eaten_piece_row, eaten_piece_col = self.get_inner_diagonal(moving_to_position, current_row, current_col)
            eaten_piece = self.piece_in_pos(eaten_piece_row, eaten_piece_col)
            self.eat_piece(eaten_piece)

            # move current piece
            for i in range(0, 2):
                current_row, current_col = self.get_inner_diagonal(moving_to_position, current_row, current_col)

            piece.move(current_row, current_col)
        
        # if not a skip
        else:
            current_row, current_col = self.get_inner_diagonal(moving_to_position, current_row, current_col)

            piece.move(current_row, current_col)
    
    def calculate_stats(self):
        '''resets the values for the number of pieces of the board'''
        red = 0
        white = 0
        red_kings = 0
        white_kings = 0

        for piece in self.pieces:
            if piece.color == "White":
                white += 1
                if piece.is_king:
                    white_kings += 1
            else:
                red += 1
                if piece.is_king:
                    red_kings += 1
        
        # reset the values
        self.red_pieces = red
        self.white_pieces = white
        self.white_kings = white_kings
        self.red_kings = red_kings
    
    def print_stats(self):
        '''prints stats for debugging purposes'''
        print("Board stats:")
        print("red: " + str(self.red_pieces))
        print("white: " + str(self.white_pieces))
        print("red kings: " + str(self.red_kings))
        print("white kings: " + str(self.white_kings))
    
    def can_be_eaten(self, piece_name):
        '''returns how many times a piece can be eaten by an enemy'''
        count = 0
        piece = self.get_piece(piece_name)
        
        if piece.color == "Red":
            enemy_color = "White"
        else:
            enemy_color = "Red"
        
        possible_moves = self.next_user_moves(self.pieces_of_color(enemy_color))
        
        for move in possible_moves:
            remaining_pieces = [piece.name for piece in move.board.pieces]
            
            # can be eaten
            if piece_name not in remaining_pieces:
                count += 1
        
        return count
    
    def calculate_score(self):
        outcome = 0
        white_pieces = self.white_pieces
        red_pieces = self.red_pieces
        
        for piece in self.pieces_of_color("White"):
            if piece.is_king:
                outcome += 8
            else:
                outcome += 5
            
            # if at edge, plus 7
            if piece.row == 0 or piece.col == 0 or piece.row == 7 or piece.col == 7:
                outcome += 7
            
            
            # if AI can be eaten, -3
            outcome -= self.can_be_eaten(piece.name) * 3
            
            # if AI can eat, plus 6
            if piece.row + 2 <= 7  and piece.col - 2 >= 0: 
                piece_check = self.piece_in_pos(piece.row + 1, piece.col - 1)
                if  piece_check != None:
                    if piece_check.color == "Red" and self.piece_in_pos(piece.row + 2, piece.col - 2) == None:
                        outcome += 6
            
            if piece.row + 2 <= 7  and piece.col + 2 <= 7:   
                piece_check = self.piece_in_pos(piece.row + 1, piece.col + 1)
                if  piece_check != None:
                    if piece_check.color == "Red" and self.piece_in_pos(piece.row + 2, piece.col + 2) == None:
                        outcome += 6
                    
            # if piece is king
            if piece.is_king:
                if piece.row - 2 >= 0  and piece.col - 2 >= 0:   
                    piece_check = self.piece_in_pos(piece.row - 1, piece.col - 1)
                    if  piece_check != None:
                        if piece_check.color == "Red" and self.piece_in_pos(piece.row - 2, piece.col - 2) == None:
                            outcome += 6
                
                if piece.row - 2 >= 0  and piece.col + 2 <= 7:  
                    piece_check = self.piece_in_pos(piece.row - 1, piece.col + 1)
                    if  piece_check != None:
                        if piece_check.color == "Red" and self.piece_in_pos(piece.row - 2, piece.col + 2) == None:
                            outcome += 6

        return outcome + (white_pieces - red_pieces) * 1000


    def choose_move(self, final_moves):
        # asks player to input user move choice
        print("-----POSSIBLE MOVES-----")
        print("note: moves are represented as [row, column]")
        choice_number = 0
        for move in final_moves:
            print("-- Choice " + str(choice_number))
            move.print_node()
            choice_number += 1
        
        print("")
        user_choice = int(input("Input choice: "))

        # loop to deal with incorrect user input
        while user_choice not in range(0, choice_number):
            print("")
            print("Choice not in options! Please try again.")
            user_choice = int(input("Input choice: "))

        print("")
        print("")
        # return node corresponding to choice
        return final_moves[user_choice]
    
    def print_board(self):
        print("---BOARD---")
        for i in range(0, 8):
            if(i == 0):
                print("     0    1    2    3    4    5    6    7")
            print(str(i) + "  ", end = "")
            for j in range(0, 8):

                # print piece in tile
                piece = self.piece_in_pos(i, j)
                if  piece != None:
                    name = piece.name
                    if piece.is_king == True:
                        name += "K"

                    print("|" + name, end = "")
                    if len(name) == 3:
                        print(" ", end = "")
                    elif len(name) == 2:
                        print("  ", end = "")
                else:
                    print("|    ", end = "")
            print("|")
        print("")

    def check_game_over(self, color_turn):
        '''returns true if there are no more pieces left or all pieces are cornered'''
        over = False

        self.calculate_stats()


        if color_turn == "White" and self.white_pieces == 0:
            over = True
        elif color_turn == "Red" and self.red_pieces == 0:
            over = True

        if self.next_user_moves(self.pieces_of_color(color_turn)) == []:
            over = True

        return over