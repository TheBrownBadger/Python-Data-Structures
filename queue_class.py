# Implementing a queue using a list
class Queue:
    # Initialize queue as empty list
    def __init__(self):
        self.items = []

    # Check if queue is empty
    def isEmpty(self):
        return self.items == []

    # To add item (enqueue)
    def enqueue(self, item):
        self.items.append(item)

    # To remove item (dequeue)
    def dequeue(self):
        return self.items.pop()

    # Return the size 
    def size(self):
        return len(self.items)

    # Show items in queue
    def show(self):
        return str(self.items)
