from AiNode import AiNode

class Tree:
    def __init__(self, root):
        self.root = root
        self.move_ordering_counter = 0
        
        # creates a tree with a depth of 3 (based on MP specs)
        root.add_children()
        
        for node in root.children:
            node.add_children()
    
    def minimax(node, depth, alpha, beta, maximizer, has_move_ordering):
        pass
    
    def print_tree():
        pass
        