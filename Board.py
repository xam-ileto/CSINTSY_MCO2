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
        
        # set remaining piece values
        self.remaining_red = 12
        self.remaining_white = 12
        self.remaining_red_kings = 0
        self.remaining_white_kings = 0
            

    def _init_this(self, board):
        # copies passed board into self
        self.pieces = deepcopy(board.pieces)
        self.remaining_red = deepcopy(board.remaining_red)
        self.remaining_white = deepcopy(board.remaining_white)
        self.remaining_red_kings = deepcopy(board.remaining_red_kings)
        self.remaining_white_kings = deepcopy(board.remaining_white_kings)

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
        # calls _is_tile_valid

        possible_moves = []
        row = piece.row
        col = piece.col
        player_color = piece.color

        possible_tiles = {}
        if piece.is_king:
            # if piece is king, check 4 diagonal tiles
            # if the diagonal tile has a piece, check the diagonal of the tile
            # upper left tile
            possible_tiles["UL"] = self._get_diagonal("UL", row, col)
            # upper right
            possible_tiles["UR"] = self._get_diagonal("UR", row, col)
            # lower left
            possible_tiles["LL"] = self._get_diagonal("LL", row, col)
            # lower right
            possible_tiles["LR"] = self._get_diagonal("LR", row, col)
        else: # piece is not a king
            if player_color == "White":
                # lower left
                possible_tiles["LL"] = self._get_diagonal("LL", row, col)
                # lower right
                possible_tiles["LR"] = self._get_diagonal("LR", row, col)
            else: # player_color == "Red"
                # upper left tile
                possible_tiles["UL"] = self._get_diagonal("UL", row, col)
                # upper right
                possible_tiles["UR"] = self._get_diagonal("UR", row, col)
        
        for position, coordinate in possible_tiles.items():
            # if position is not valid, continue (no need to check)
            coordinate_row = coordinate[0]
            coordinate_col = coordinate[1]
            if self._is_tile_valid(coordinate_row, coordinate_col) == False:
                continue

            # if no piece in tile, add to possible moves
            piece_in_diagonal = self._piece_in_pos(coordinate_row, coordinate_col)
            if  piece_in_diagonal == None:
                possible_moves.append(coordinate)
            
            # else if there is a piece of opposite color, check diagonal tile
            # if no piece in diagonal tile, add to possible moves
            elif piece_in_diagonal._is_enemy_piece(player_color):
                if position == "UL":
                    skip_coordinates = self._get_diagonal("UL", coordinate_row, coordinate_col)
                elif position == "UR":
                    skip_coordinates = self._get_diagonal("UR", coordinate_row, coordinate_col)
                elif position == "LL":
                    skip_coordinates = self._get_diagonal("LL", coordinate_row, coordinate_col)
                elif position == "LR":
                    skip_coordinates = self._get_diagonal("LR", coordinate_row, coordinate_col)

                # if skip_coordinates is not valid, continue
                if self._is_tile_valid(skip_coordinates[0], skip_coordinates[1]) == False:
                    continue

                if self._piece_in_pos(skip_coordinates[0], skip_coordinates[1]) == None:
                    possible_moves.append(skip_coordinates)
                
        
        # return the list of possible moves
        return possible_moves
        

    def _is_tile_valid(self, row, col):
        # checks if a passed position goes out of bounds
        if row < 0 or row > 7 or col < 0 or col > 7:
            # return false if out of bounds
            return False
        
        # return true if within bounds
        return True
    
    def _eat_piece(self, piece):
        self.pieces.remove(piece)

    def _piece_in_pos(self, row, col):
        for piece in self.pieces:
            if piece.col == col and piece.row == row:
                return piece
        
        return None

    def get_piece(self, name):
        # this does not take into account if the piece is a king
        for piece in self.pieces:
            if piece.name == name:
                return piece

    def _get_diagonal(self, diagonal, row, col):
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

    def _next_user_moves(self, player_pieces):
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
            board = deepcopy(self)
            
            stack = deque() 

            print("we are looking at piece " + piece.name)

            ctr = 0
            for move in self.next_piece_moves(piece):
                # create node and starting board
                start_node = NodeUserMoves(piece.name, self, root_row, root_col)
                stack.append(start_node)
                # add next move to the node
                print("move: " + str(move[0]) + " " + str(move[1]))

                new_board = Board(self)
                print("piece original location " + str(start_node.board_moves[0].get_piece(piece.name).row) + " " + str(start_node.board_moves[0].get_piece(piece.name).col) )

                new_board.simulate_move(new_board.get_piece(piece.name), move[0], move[1])
                
                start_node.add_move(new_board, move[0], move[1])
                print("R3 location: " + str(new_board.get_piece("R3").row) + " " + str(new_board.get_piece("R3").col))
                new_board.print_board()
                ctr +=1

                
                if piece.name == "R3":
                    print("--------------R3-----------------")
                    print("R3 position in board 1: " + str(start_node.board_moves[0].get_piece("R3").row) + " " + str(start_node.board_moves[0].get_piece("R3").col))
                    print("R3 position in board 2: " + str(start_node.board_moves[1].get_piece("R3").row) + " " + str(start_node.board_moves[1].get_piece("R3").col))
                print("")
            
            continue
            moves_nonfinal = self.next_piece_moves(piece)
            number_of_moves = len(moves_nonfinal)
            print(moves_nonfinal)
            for i in range(0, number_of_moves):
                # create node and starting board
                start_node = NodeUserMoves(piece.name, self, root_row, root_col)
                stack.append(start_node)
                # add next move to the node
                print("move: " + str(moves_nonfinal[i][0]) + " " + str(moves_nonfinal[i][1]))

                new_board = Board(self)
                new_board.simulate_move(new_board.get_piece(piece.name))

                print("piece original location " + str(start_node.moved_piece.row) + " " + str(start_node.moved_piece.col))
                new_board.simulate_move(start_node.moved_piece, moves_nonfinal[i][0],moves_nonfinal[i][1])
                start_node.add_move(new_board, moves_nonfinal[i][0], moves_nonfinal[i][1])
                print("R3 location: " + str(new_board.get_piece("R3").row) + " " + str(new_board.get_piece("R3").col))
                new_board.print_board()
                


            continue
            # this is the old code
            # check the possible moves for each movable piece
            for move in self.next_piece_moves(piece):

                # create node and starting board
                start_node = NodeUserMoves(piece, self, root_row, root_col)
                stack.append(start_node)
                # add next move to the node
                print("move: " + str(move[0]) + " " + str(move[1]))
                new_board = Board(self)
                print("piece original location " + str(piece.row) + " " + str(piece.col))
                new_board.simulate_move(piece, move[0],move[1])
                start_node.add_move(new_board, move[0], move[1])
                print("R3 location: " + str(new_board.get_piece("R3").row) + " " + str(new_board.get_piece("R3").col))
                new_board.print_board()
            
            print("")
            
            continue
            # for debugging
            for node in stack:
                node.print_node()
                print(len(node.board_moves))
                node.get_final_board().print_board()

            # break
            continue

            
            print("number of possible moves: " + str(len(stack)))
            # TO DO
            while(len(stack) != 0): # while there are still explorable nodes, keep exploring
                current_node = stack.pop()
                print("checking node for move " + str(current_node.get_final_move()[0]) + " " + str(current_node.get_final_move()[1]))
                current_board = current_node.get_final_board()
                current_row = current_node.get_final_move()[0]
                current_col = current_node.get_final_move()[1]

                print("this is the current board")
                current_board.print_board()

                print("simulating next move")
                # simulate the next board with next move
                # next_board = Board(self)
                # next_board.simulate_move(current_node.piece, )

                
                print("is next_piece_moves empty: " + str(len(current_board.next_piece_moves(current_board.get_piece(current_node.moved_piece.name))) == 0))
                # if next_piece_moves is empty && row, col are different from root row col,
                # add move to node and add to final_possible_moves, then pop from stack
                if (current_board.next_piece_moves(current_board.get_piece(current_node.moved_piece.name)) == []):
                    print("this node still has possible moves")

                # else, add move to node and add to stack
                else:
                    print("piece " + current_node.moved_piece.name + " has no more possible moves")

                # do for everything
            print("")
        
    def _get_inner_diagonal(self, position, row, col):
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
    
    def _check_is_skip(self, piece, row):
        if (row  == piece.row - 2 or row == piece.row + 2):
            return True
        
        # else
        return False
    
    def _check_which_diagonal(self, piece, row, col):
        current_row = piece.row
        current_col = piece.col

        # returns string of position of tile (ex. "UR"/"UL")
        # thsi is regardless if inner or outer position
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
        is_skip = self._check_is_skip(piece, row)

        moving_to_position = self._check_which_diagonal(piece, row, col)
        print(moving_to_position)
        print("is skip? " + str(is_skip))
        print("og row " + str(current_row))
        print("new row " + str(row))

        if (is_skip):
            # eat enemy
            eaten_piece_row, eaten_piece_col = self._get_inner_diagonal(moving_to_position, current_row, current_col)
            print(eaten_piece_row)
            print(eaten_piece_col)
            eaten_piece = self._piece_in_pos(eaten_piece_row, eaten_piece_col)
            self._eat_piece(eaten_piece)

            # move current piece
            for i in range(0, 2):
                current_row, current_col = self._get_inner_diagonal(moving_to_position, current_row, current_col)

            print("moving piece to " + str(current_row) + " " + str(current_col))
            print("current row, current col: " + str(current_row) + " " + str(current_col))
            piece.move(current_row, current_col)
        
        # if not a skip
        else:
            current_row, current_col = self._get_inner_diagonal(moving_to_position, current_row, current_col)

            piece.move(current_row, current_col)


    def choose_move():
        # calls _next_user_moves
        # need to tell user to omit the K when inputting if the piece is a king
        pass
    
    def print_board(self):
        print("---BOARD---")
        for i in range(0, 8):
            if(i == 0):
                print("     0    1    2    3    4    5    6    7")
            print(str(i) + "  ", end = "")
            for j in range(0, 8):

                # print piece in tile
                piece = self._piece_in_pos(i, j)
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
