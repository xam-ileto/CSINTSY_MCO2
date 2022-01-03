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
        