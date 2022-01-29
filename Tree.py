from AiNode import AiNode

class Tree:
    def __init__(self, root, max_depth):
        self.root = root
        # counter = for counting the number of nodes explored in minimax
        self.counter = 0
        self.max_depth = max_depth
        # number_of_nodes = total number of nodes in the tree
        self.number_of_nodes = 0
        
        
    def minimax(self, node, depth, alpha, beta, maximizer, has_move_ordering):
        '''performs the minimax algorithm and builds the tree as minimax is being performed'''
        # turn is either "White" or "Red" depending on whose turn it is
        if maximizer:
            turn = "White"
        else:
            turn = "Red"
        
        
        # generate children if node is non-leaf
        if node.depth < self.max_depth:
            node.add_children()
            
            # if move ordering is specified, sort the children
            if has_move_ordering:
                node.sort_children_descending()
        self.counter += 1
        
        if depth == 0 or node.board.check_game_over(turn):
            return node, node.score
        
        if maximizer:
            maxEval = float('-inf')
            maxEval_node = node
            for child in node.children:
                eval_node, score = self.minimax(child, depth - 1, alpha, beta, False, has_move_ordering)
                
                original_maxEval = maxEval
                maxEval = max(maxEval, score)
                
                if maxEval == score and maxEval != original_maxEval:
                    maxEval_node = eval_node
                
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
                
            return maxEval_node, maxEval
        else: # if turn == "Red"
            minEval = float('inf')
            minEval_node = node
            for child in node.children:
                
                eval_node, score = self.minimax(child, depth - 1, alpha, beta, True, has_move_ordering)
                original_minEval = minEval
                minEval = min(minEval, score)
                
                if minEval == score and minEval != original_minEval:
                    minEval_node.node = eval_node
                
                beta = min(beta, score)
                if beta <= alpha:
                    break
                
            return minEval_node, minEval
    
    def count_nodes(self, visited_nodes, node):
        '''counts the total number of nodes'''
        if node not in visited_nodes:
            self.number_of_nodes += 1
            visited_nodes.append(node)
            for child in node.children:
                self.count_nodes(visited_nodes, child)