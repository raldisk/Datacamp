class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find_min(self):
        # Set current_node as the root
        current_node = self.root
        # Iterate over the nodes of the appropriate subtree
        while current_node.left_child:
            # Update current_node
            current_node = current_node.left_child
        return current_node.data


bst = CreateTree()
print(bst.find_min())
