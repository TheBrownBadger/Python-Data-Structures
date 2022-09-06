# Implementing a node class for a linked list
class Node:
    # Initialize node object and set the reference \
    # to the next node as None
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # Return the data within the node
    def getData(self):
        return self.data

    # Return the data of the next node
    def getNext(self):
        return self.next

    # Set the data of the current node
    def setData(self, newdata):
        self.data = newdata

    # Set the data of the next node
    def setNext(self, newnext):
        self.next = newnext
