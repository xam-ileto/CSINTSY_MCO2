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
        # print("node depth: " + str(node.depth))
        # print("max depth: " + str(self.max_depth))
        if node.depth < self.max_depth: # and node.children == []:
            # print("adding children")
            node.add_children()
            
            # if move ordering is specified, sort the children
            if has_move_ordering:
                node.sort_children_descending()
        # print("number of children: " + str(len(node.children)))
        self.counter += 1
        
        # print('at node  (s = ' + str(node.score) + ', d = ' + str(depth) + '): a = ' + str(alpha) + ', b = ' + str(beta))
            
        # print("depth " + str(depth))
        if depth == 0 or node.board.check_game_over(turn):
            # print("in if")
            print('score ' + str(node.score))
            return node, node.score
        
        if maximizer:
            maxEval = float('-inf')
            maxEval_node = node
            # counter = 0
            for child in node.children:
                eval_node, score = self.minimax(child, depth - 1, alpha, beta, False, has_move_ordering)
                # counter += 1
                
                original_maxEval = maxEval
                maxEval = max(maxEval, score)
                
                # print("counter " + str(counter))
                if maxEval == score and maxEval != original_maxEval:
                    maxEval_node = eval_node
                
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
                
                print('at node  (s = ' + str(node.score) + ', d = ' + str(depth) + '): a = ' + str(alpha) + ', b = ' + str(beta))
            # print(maxEval_node.board.print_board())
            # print(maxEval_node.depth)
            print("----------depth " + str(node.depth) + " final maximum score found: " + str(maxEval_node.score))
            return maxEval_node, maxEval
        else: # if turn == "Red" (original)
            minEval = float('inf')
            minEval_node = node
            for child in node.children:
                
                eval_node, score = self.minimax(child, depth - 1, alpha, beta, True, has_move_ordering)
                # print("compare to " + str(score))
                original_minEval = minEval
                minEval = min(minEval, score)
                # print("minimum score found: " + str(minEval))
                # print("")
                
                if minEval == score and minEval != original_minEval:
                    minEval_node.node = eval_node
                
                beta = min(beta, score)
                if beta <= alpha:
                    break
                
                print('at node  (s = ' + str(node.score) + ', d = ' + str(depth) + '): a = ' + str(alpha) + ', b = ' + str(beta))
            # print(minEval_node.board.print_board())
            # print(minEval_node.depth)
            print("----------depth " + str(node.depth) + " final minimum score found: " + str(minEval_node.score))
            return minEval_node, minEval
    
    def minimax_no_pruning(self, node, depth, maximizer, has_move_ordering):
        '''performs the minimax algorithm and builds the tree as minimax is being performed'''
        # turn is either "White" or "Red" depending on whose turn it is
        if maximizer:
            turn = "White"
        else:
            turn = "Red"
        
        
        # generate children if node is non-leaf
        # print("node depth: " + str(node.depth))
        # print("max depth: " + str(self.max_depth))
        if node.depth < self.max_depth: # and node.children == []:
            print("adding children")
            node.add_children()
            
            # if move ordering is specified, sort the children
            if has_move_ordering:
                node.sort_children_descending()
        print("number of children: " + str(len(node.children)))
        self.counter += 1
        
        # print('at node  (s = ' + str(node.score) + ', d = ' + str(depth) + '): a = ' + str(alpha) + ', b = ' + str(beta))
            
        print("depth " + str(depth))
        if depth == 0 or node.board.check_game_over(turn):
            print("in if")
            print('score ' + str(node.score))
            return node, node.score
        
        if maximizer:
            maxEval = float('-inf')
            maxEval_node = node
            # counter = 0
            for child in node.children:
                eval_node, score = self.minimax_no_pruning(child, depth - 1, False, has_move_ordering)
                # counter += 1
                
                original_maxEval = maxEval
                maxEval = max(maxEval, score)
                
                # print("counter " + str(counter))
                if maxEval == score and maxEval != original_maxEval:
                    maxEval_node = eval_node
                
                
            # print(maxEval_node.board.print_board())
            # print(maxEval_node.depth)
            print("----------depth " + str(node.depth) + " final maximum score found: " + str(maxEval_node.score))
            return maxEval_node, maxEval
        else: # if turn == "Red" (original)
            minEval = float('inf')
            minEval_node = node
            for child in node.children:
                
                eval_node, score = self.minimax_no_pruning(child, depth - 1, True, has_move_ordering)
                # print("compare to " + str(score))
                original_minEval = minEval
                minEval = min(minEval, score)
                # print("minimum score found: " + str(minEval))
                # print("")
                
                if minEval == score and minEval != original_minEval:
                    minEval_node.node = eval_node
                
                
            # print(minEval_node.board.print_board())
            # print(minEval_node.depth)
            print("----------depth " + str(node.depth) + " final minimum score found: " + str(minEval_node.score))
            return minEval_node, minEval
    
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
        