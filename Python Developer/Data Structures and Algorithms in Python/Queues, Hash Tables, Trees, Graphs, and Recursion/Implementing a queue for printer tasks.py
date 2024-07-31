# 1/3
class PrinterTasks:
    def __init__(self):
        self.queue = Queue()

    def add_document(self, document):
        # Add the document to the queue
        self.queue.enqueue(document)

    def print_documents(self):
        # Iterate over the queue while it has elements
        while self.queue.has_elements():
            # Remove the document from the queue
            print("Printing", self.queue.dequeue())


# 2/3
printer_tasks = PrinterTasks()
# Add some documents to print
printer_tasks.add_document("Document 1")
printer_tasks.add_document("Document 2")
printer_tasks.add_document("Document 3")
# Print all the documents in the queue
printer_tasks.print_documents()


# 3/3
# 0(1)
