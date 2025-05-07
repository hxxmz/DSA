class DoublyNode:
    def __init__(self, value, next_value=None, prev_value=None):
        self.value = value
        self.next = next_value
        self.prev = prev_value
    
    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self, data=None):
        """
        Initializes the doubly linked list with an optional starting node value.
        """
        new_node = None
        if data is not None:
            new_node = DoublyNode(data)
        self.head = new_node
        self.tail = new_node

    def prepend(self, data):
        """
        Prepends a new node with the given data at the beginning of the list.
        
        :param data: The value to insert at the beginning of the list.
        :return: True if the operation was successful, otherwise False.
        """
        if data is None:
            print("Cannot prepend None value.")
            return False

        new_node = DoublyNode(data)
        # If the list is empty, new node becomes both head and tail
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            print(f"Prepended node with value '{data}' to the empty list.")
            return True
        
        # Linking the new node at the beginning of the list
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        print(f"Prepended node with value '{data}' to the list.")
        return True

    def append(self, data):
        """
        Appends a new node with the given data at the end of the list.
        
        :param data: The value to insert at the end of the list.
        :return: True if the operation was successful, otherwise False.
        """
        if data is None:
            print("Cannot append None value.")
            return False

        new_node = DoublyNode(data)
        # If the list is empty, new node becomes both head and tail
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            print(f"Appended node with value '{data}' to the empty list.")
            return True
        
        # Linking the new node at the end of the list
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

        print(f"Appended node with value '{data}' to the list.")
        return True

    def is_empty(self):
        """
        Checks whether the doubly linked list is empty.
        
        :return: True if the list is empty, otherwise False.
        """
        pass

    def insert_after(self, prev_value, data):
        """
        Inserts a new node with the given data after the node with the specified value.
        
        :param prev_value: The value of the node after which to insert the new node.
        :param data: The value to insert.
        :return: True if the operation was successful, otherwise False.
        """
        pass

    # add insert_before

    def delete(self, key):
        """
        Deletes the node with the specified key.
        
        :param key: The value of the node to be deleted.
        :return: True if the operation was successful, otherwise False.
        """
        pass

    def search(self, key):
        """
        Searches for a node with the specified key.
        
        :param key: The value to search for in the list.
        :return: True if the node is found, otherwise False.
        """
        pass

    def find_node(self, key):
        """
        Finds the node with the specified key.
        
        :param key: The value to search for in the list.
        :return: The node if found, otherwise None.
        """
        pass

    def edit_node(self, key, data):
        """
        Edits the node with the specified key by updating its value.
        
        :param key: The value of the node to be edited.
        :param data: The new value to set for the node.
        :return: True if the operation was successful, otherwise False.
        """
        pass

    def get_length(self):
        """
        Gets the number of nodes in the list.
        
        :return: The length of the list.
        """
        pass

    def print_list(self):
        """
        Prints the nodes in the list from head to tail.
        """
        pass

    def print_reverse(self):
        """
        Prints the nodes in the list from tail to head.
        """
        pass