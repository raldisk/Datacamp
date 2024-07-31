# Removing the first node from a linked list


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_at_beginning(self):
        # The "next" node of the head becomes the new head node
        self.head = self.head.next
