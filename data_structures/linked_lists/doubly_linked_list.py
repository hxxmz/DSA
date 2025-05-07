class DoublyNode:
    def __init__(self, value, next_value=None, prev_value=None):
        self.value = value
        self.next = next_value
        self.prev = prev_value
    
    def __str__(self):
        return str(self.value)

