from AiNode import AiNode
from Board import Board
from AiNode import AiNode
from Tree import Tree
import time

b = Board("Start")

DEPTH = 2
DEPTHS = [2,3,4]

# set up board
white = []
for piece in b.pieces_of_color("White"):
    if piece.name in white:
        b.eat_piece(b.get_piece(piece.name))

red = []
for piece in b.pieces_of_color("Red"):
    if piece.name in red:
        b.eat_piece(b.get_piece(piece.name))
        
b.get_piece("R1").move(4,1)
b.get_piece("R5").move(5,0)
b.get_piece("W9").move(3,0)

b.calculate_stats()
b.print_board()

for DEPTH in DEPTHS:
    print("IN DEPTH " + str(DEPTH) + "*************************")
    
    # # With move ordering
    # print("WITH MOVE ORDERING")
    # root = AiNode(b, 0, "White")
    # tree = Tree(root, DEPTH)
    # start = time.time()
    # move, move_score = tree.minimax(tree.root,DEPTH,-100000,100000,True,True)
    # end = time.time()
    # total_time = end - start
    # print("time: " + str(total_time))

    # visited = []
    # tree.print_tree(visited, tree.root)

    # print("nodes explored: " + str(tree.counter))
    # visited = []
    # tree.count_nodes(visited, tree.root)
    # print("total nodes: " + str(tree.number_of_nodes))
    # print("")

    # Without move ordering
    print("WITHOUT MOVE ORDERING")
    new_root = AiNode(b, 0, "White")
    new_tree = Tree(new_root, DEPTH)
    start = time.time()
    move, move_score = new_tree.minimax(new_tree.root,DEPTH,-100000,100000,True,False)
    end = time.time()
    total_time = end - start
    print("time: " + str(total_time))

    visited = []
    new_tree.print_tree(visited,new_tree.root)

    # print("nodes explored: " + str(new_tree.counter))
    # visited = []
    # new_tree.count_nodes(visited, new_tree.root)
    # print("total nodes: " + str(new_tree.number_of_nodes))
    # print("")

    # # No pruning, with ordering
    # print("NO PRUNING, WITH ORDERING")
    # root3 = AiNode(b, 0, "White")
    # tree3 = Tree(root, DEPTH)
    # start = time.time()
    # move, move_score = tree3.minimax_no_pruning(tree3.root, DEPTH, True, True)
    # end = time.time()
    # total_time = end - start
    # print("time: " + str(total_time))

    # visited = []
    # tree3.count_nodes(visited, tree3.root)

    # # visited = []
    # # tree3.print_tree(visited, tree3.root)
    # print("total nodes: " + str(tree3.number_of_nodes))
    # print("")

    # # No pruning, without ordering
    # print("NO PRUNING, WITHOUT ORDERING")
    # root4 = AiNode(b, 0, "White")
    # tree4 = Tree(root, DEPTH)
    # start = time.time()
    # move, move_score = tree4.minimax_no_pruning(tree4.root, DEPTH, True, True)
    # end = time.time()
    # total_time = end - start
    # print("time: " + str(total_time))

    # # visited = []
    # # tree4.print_tree(visited, tree4.root)

    # visited = []
    # tree4.count_nodes(visited, tree4.root)
    # print("total nodes: " + str(tree4.number_of_nodes))
    # print("")
    print("")