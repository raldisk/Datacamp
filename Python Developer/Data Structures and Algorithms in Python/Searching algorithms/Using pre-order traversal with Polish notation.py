class ExpressionTree:
    def __init__(self):
        self.root = None

    def pre_order(self, current_node):
        # Check if current_node exists
        if current_node:
            # Print the value of the current_node
            print(current_node.data)
            # Call pre_order recursively on the appropriate half of the tree
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)


et = CreateExpressionTree()
et.pre_order(et.root)
