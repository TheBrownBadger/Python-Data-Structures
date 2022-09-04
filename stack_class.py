## Implementation of a stack using a list
# Stack
class Stack:
    # Initialize stack as empty list
    def __init__(self):
        self.items = []

    # Checking if empty
    def isEmpty(self):
        return self.items == []

    # Push onto the stack
    def push(self, item):
        self.items.append(item)

    # Popping the stack
    def pop(self):
        return self.items.pop()

    # Return the size
    def size(self):
        return len(self.items)

    # Show the contents
    def show(self):
        return str(self.items)
