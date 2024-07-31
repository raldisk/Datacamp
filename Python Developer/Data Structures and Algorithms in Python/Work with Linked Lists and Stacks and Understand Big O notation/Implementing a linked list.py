# 1/3
class Node:
    def __init__(self, data):
        # Store the value for the node
        self.value = data


# 2/3
class Node:
    def __init__(self, data):
        self.value = data
        # Leave the node initially without a next value
        self.next = None


# 3/3
class LinkedList:
    def __init__(self):
        # Set the head and the tail with null values
        self.head = None
        self.tail = None
