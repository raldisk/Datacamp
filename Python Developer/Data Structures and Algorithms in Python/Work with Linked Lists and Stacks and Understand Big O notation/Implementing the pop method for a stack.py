# 1/2
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):
        # Check if there is a top element
        if self.top is None:
            return None
        else:
            popped_node = self.top
            # Decrement the size of the stack
            self.size -= 1
            # Update the new value for the top node
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data


# 2/2
# 0(1)
