from AiNode import AiNode

class Tree:
    def __init__(self, root, max_depth):
        self.root = root
        self.counter = 0
        self.max_depth = max_depth
        self.number_of_nodes = 0
        
    
    def minimax(self, node, depth, alpha, beta, turn):
        # turn is either "White" or "Red" depending on whose turn it is
        
        # generate children
        print("depth: " + str(node.depth))
        if node.depth < self.max_depth and node.children == []:
            node.add_children()
        
        self.counter += 1
            
            
        if depth == self.max_depth or node.board.check_game_over(turn):
            return node
        
        if turn == "White":
            maxEval = float('-inf')
            maxEval_node = node
            for child in node.children:
                eval_node = self.minimax(child, depth + 1, alpha, beta, "Red")
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
                
                eval_node = self.minimax(child, depth + 1, alpha, beta, "White")
                minEval = min(minEval, eval_node.score)
                
                if minEval == eval_node.score:
                    minEval_node.node = eval_node
                
                beta = min(beta, eval_node.score)
                if beta <= alpha:
                    break
            return minEval_node
    
    def move_ordering(self, visited_nodes, node):
        '''sorts all nodes in descending order'''
        if node not in visited_nodes:
            node.sort_children_descending()
            visited_nodes.append(node)
            for child in node.children:
                self.move_ordering(visited_nodes, child)
    
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
        