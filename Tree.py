from AiNode import AiNode

class Tree:
    def __init__(self, root):
        self.root = root
        self.ordering_counter = 0
        self.no_ordering_counter = 0
        
        # creates a tree with a depth of 3 (based on MP specs)
        root.add_children()
        for node in root.children:
            node.add_children()
    
    def minimax(self, node, depth, alpha, beta, turn, counter):
        print("at depth: " + str(depth))
        # turn is either "White" or "Red" depending on whose turn it is
        
        # only counts the nodes at depth 2
        if node.depth == 2:
            if counter == True:
                self.ordering_counter += 1
            else:
                self.no_ordering_counter += 1
            
            if depth == 2 or node.board.check_game_over(turn):
                # print("returned a " + str(type(node)))
                return node
        
        if turn == "White":
            # print("at white")
            # print("a: " + str(alpha) + "   b: " + str(beta))
            maxEval = float('-inf')
            maxEval_node = node
            for child in node.children:
                eval_node = self.minimax(child, depth + 1, alpha, beta, "Red", counter)
                # print(type(eval_node))
                maxEval = max(maxEval, eval_node.score)
                
                if maxEval == eval_node.score:
                    maxEval_node = eval_node
                
                alpha = max(alpha, eval_node.score)
                if beta <= alpha:
                    break
            # print("a: " + str(alpha) + "   b: " + str(beta))
            return maxEval_node
        else: # if turn == "Red"
            # print("at red")
            # print("a: " + str(alpha) + "   b: " + str(beta))
            minEval = float('inf')
            minEval_node = node
            for child in node.children:
                
                eval_node = self.minimax(child, depth + 1, alpha, beta, "White", counter)
                # print(type(eval_node))
                minEval = min(minEval, eval_node.score)
                
                if minEval == eval_node.score:
                    minEval_node.node = eval_node
                
                beta = min(beta, eval_node.score)
                if beta <= alpha:
                    break
            # print("a: " + str(alpha) + "   b: " + str(beta))
            return minEval_node
    
    def move_ordering(self):
        '''sorts depth 3 nodes in descending order'''
        # self.root.sort_children_descending()
        
        for depth1_node in self.root.children:
            depth1_node.sort_children_descending()
    
    def print_tree(self):
        self.root.print_node()
        
        for depth2 in self.root.children:
            depth2.print_node()
            
            for depth3 in depth2.children:
                depth3.print_node()
        