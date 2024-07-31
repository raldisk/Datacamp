# 1/2

# Implementing a Stack with the push method
class Stack:
    def __init__(self):
        # Initially there won't be any node at the top of the stack
        self.top = None
        # Initially there will be zero elements in the stack
        self.size = 0


# 2/2


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        # Create a node with the data
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        # Set the created node to the top node
        self.top = new_node
        # Increase the size of the stack by one
        self.size += 1
