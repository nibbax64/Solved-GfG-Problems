class LinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def copy(self):
        return self
