from AiNode import AiNode

class Tree:
    def __init__(self, root):
        self.root = root
        self.move_ordering_counter = 0
        
        # creates a tree with a depth of 3 (based on MP specs)
        root.add_children()
        for node in root.children:
            node.add_children()
    
    def minimax(self, node, depth, alpha, beta, turn, has_move_ordering):
        print("at depth: " + str(depth))
        # turn is either "White" or "Red" depending on whose turn it is
        
        # if minimax has move ordering, sort nodes in descending order
        if has_move_ordering:
            self.move_ordering()
        
        if depth == 2 or node.board.check_game_over(turn):
            # print("returned a " + str(type(node)))
            return node
        
        if turn == "White":
            print("at white")
            maxEval = float('-inf')
            maxEval_node = node
            for child in node.children:
                eval_node = self.minimax(child, depth + 1, alpha, beta, "Red", has_move_ordering)
                # print(type(eval_node))
                maxEval = max(maxEval, eval_node.score)
                
                if maxEval == eval_node.score:
                    maxEval_node = eval_node
                
                alpha = max(alpha, eval_node.score)
                if beta <= alpha:
                    break
            return maxEval_node
        else: # if turn == "Red"
            print("at red")
            minEval = float('inf')
            minEval_node = node
            for child in node.children:
                
                eval_node = self.minimax(child, depth + 1, alpha, beta, "White", has_move_ordering)
                # print(type(eval_node))
                minEval = max(minEval, eval_node.score)
                
                if minEval == eval_node.score:
                    minEval_node.node = eval_node
                
                beta = max(beta, eval_node.score)
                if beta <= alpha:
                    break
            return minEval_node
    
    def move_ordering(self):
        '''orders all nodes of tree in descending order'''
        self.root.sort_children_descending()
        
        for depth2_node in self.root.children:
            depth2_node.sort_children_descending()
            
            for depth3_node in depth2_node.children:
                depth3_node.sort_children_descending()
    
    def print_tree(self):
        self.root.print_node()
        
        for depth2 in self.root.children:
            depth2.print_node()
            
            for depth3 in depth2.children:
                depth3.print_node()
        