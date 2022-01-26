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
        if node.depth < self.max_depth: # and node.children == []:
            node.add_children()
            
            # if move ordering is specified, sort the children
            if has_move_ordering:
                node.sort_children_descending()
        
        self.counter += 1
        
        # print('at node  (s = ' + str(node.score) + ', d = ' + str(depth) + '): a = ' + str(alpha) + ', b = ' + str(beta))
            
            
        if depth == self.max_depth or node.board.check_game_over(turn):
            return node
        
        if maximizer:
            print('in maximizer')
            maxEval = float('-inf')
            maxEval_node = node
            # counter = 0
            for child in node.children:
                eval_node = self.minimax(child, depth + 1, alpha, beta, False, has_move_ordering)
                # counter += 1
                
                original_maxEval = maxEval
                maxEval = max(maxEval, eval_node.score)
                
                # print("counter " + str(counter))
                if maxEval == eval_node.score and maxEval != original_maxEval:
                    maxEval_node = eval_node
                
                alpha = max(alpha, eval_node.score)
                if beta <= alpha:
                    break
                
                print('at node  (s = ' + str(node.score) + ', d = ' + str(depth) + '): a = ' + str(alpha) + ', b = ' + str(beta))
            # print(maxEval_node.board.print_board())
            # print(maxEval_node.depth)
            print("----------depth 0 final maximum score found: " + str(maxEval_node.score))
            return maxEval_node
        else: # if turn == "Red" (original)
            print("in minimizer")
            minEval = float('inf')
            minEval_node = node
            for child in node.children:
                
                eval_node = self.minimax(child, depth + 1, alpha, beta, True, has_move_ordering)
                # print("compare to " + str(eval_node.score))
                original_minEval = minEval
                minEval = min(minEval, eval_node.score)
                # print("minimum score found: " + str(minEval))
                # print("")
                
                if minEval == eval_node.score and minEval != original_minEval:
                    minEval_node.node = eval_node
                
                beta = min(beta, eval_node.score)
                if beta <= alpha:
                    break
                
                print('at node  (s = ' + str(node.score) + ', d = ' + str(depth) + '): a = ' + str(alpha) + ', b = ' + str(beta))
            # print(minEval_node.board.print_board())
            # print(minEval_node.depth)
            print("----------depth 1 final minimum score found: " + str(minEval_node.score))
            return minEval_node
    
    def original_minimax(self, node, depth, alpha, beta, turn, has_move_ordering):
        '''performs the minimax algorithm and builds the tree as minimax is being performed'''
        # turn is either "White" or "Red" depending on whose turn it is
        
        # generate children if node is non-leaf
        if node.depth < self.max_depth: # and node.children == []:
            node.add_children()
            
            # if move ordering is specified, sort the children
            if has_move_ordering:
                node.sort_children_descending()
        
        self.counter += 1
            
            
        if depth == self.max_depth or node.board.check_game_over(turn):
            return node
        
        if turn == "White":
            maxEval = float('-inf')
            maxEval_node = node
            for child in node.children:
                eval_node = self.minimax(child, depth + 1, alpha, beta, "Red", has_move_ordering)
                maxEval = max(maxEval, eval_node.score)
                
                if maxEval == eval_node.score:
                    maxEval_node = eval_node
                
                alpha = max(alpha, eval_node.score)
                if beta <= alpha:
                    break
            return maxEval_node
        else: # if turn == "Red"
            minEval = float('inf')
            minEval_node = node
            for child in node.children:
                
                eval_node = self.minimax(child, depth + 1, alpha, beta, "White", has_move_ordering)
                minEval = min(minEval, eval_node.score)
                
                if minEval == eval_node.score:
                    minEval_node.node = eval_node
                
                beta = min(beta, eval_node.score)
                if beta <= alpha:
                    break
            return minEval_node
    
    def minimaxOld(self, node, depth, alpha, beta, maximizer, has_move_ordering):
        '''performs the minimax algorithm and builds the tree as minimax is being performed'''
        # turn is either "White" or "Red" depending on whose turn it is
        if maximizer:
            turn = "White"
        else:
            turn = "Red"
        

        
        # generate children if node is non-leaf
        if node.depth < self.max_depth: # and node.children == []:
            node.add_children()
            
            # if move ordering is specified, sort the children
            if has_move_ordering:
                node.sort_children_descending()
        
        self.counter += 1
        
        # print("at node " + str(self.counter) + ' (s = ' + str(node.score) + ', d = ' + str(depth) + '): a = ' + str(alpha) + ', b = ' + str(beta))
            
            
        if depth == self.max_depth or node.board.check_game_over(turn):
            return node
        
        if maximizer:
            maxEval = float('-inf')
            maxEval_node = node
            for child in node.children:
                eval_node = self.minimax(child, depth + 1, alpha, beta, False, has_move_ordering)
                maxEval = max(maxEval, eval_node.score)
                
                if maxEval == eval_node.score:
                    maxEval_node = eval_node
                
                alpha = max(alpha, eval_node.score)
                if beta <= alpha:
                    break
            
            # print(maxEval_node.board.print_board())
            # print(maxEval_node.depth)
            return maxEval_node
        else: # if turn == "Red" (original)
            minEval = float('inf')
            minEval_node = node
            for child in node.children:
                
                eval_node = self.minimax(child, depth + 1, alpha, beta, True, has_move_ordering)
                minEval = min(minEval, eval_node.score)
                
                if minEval == eval_node.score:
                    minEval_node.node = eval_node
                
                beta = min(beta, eval_node.score)
                if beta <= alpha:
                    break
            # print(minEval_node.board.print_board())
            # print(minEval_node.depth)
            return minEval_node
    
    def count_nodes(self, visited_nodes, node):
        '''counts the total number of nodes'''
        if node not in visited_nodes:
            self.number_of_nodes += 1
            visited_nodes.append(node)
            for child in node.children:
                self.count_nodes(visited_nodes, child)
    
    def print_tree(self, visited_nodes, node):
        '''For debugging purposes: prints tree using DFS'''
        if node not in visited_nodes:
            node.print_node()
            visited_nodes.append(node)
            for child in node.children:
                self.print_tree(visited_nodes, child)
    
    def print_tree_depth(self, visited_nodes, node, depth):
        '''For debugging purposes: prints tree using DFS'''
        if node not in visited_nodes:
            if node.depth == depth:
                node.print_node()
            visited_nodes.append(node)
            for child in node.children:
                self.print_tree_depth(visited_nodes, child, depth)
        