# Implementing a deque using a list
class Deque:
    # Initialize deque as empty list
    def __init__(self):
        self.items = []

    # Check whether deque is empty
    def isEmpty(self):
        return self.items == []

    # Add item the front
    def addFront(self, item):
        self.items.append(item)

    # Add item the rear
    def addRear(self, item):
        self.items.insert(0, item)

    # Remove item from the front
    def removeFront(self):
        return self.items.pop()

    # Remove item from the rear
    def removeRear(self):
        return self.items.pop(0)

    # Return the size 
    def size(self):
        return len(self.items)

    # Show the items in deque
    def show(self):
        return str(self.items)
