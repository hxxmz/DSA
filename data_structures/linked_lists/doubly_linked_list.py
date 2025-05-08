class DoublyNode:
    def __init__(self, value, next_value=None, prev_value=None):
        self.value = value
        self.next = next_value
        self.prev = prev_value
    
    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    # ========================== Initialization ==========================
    def __init__(self, data=None):
        """
        Initializes the doubly linked list with an optional starting node value.
        """
        new_node = None
        if data is not None:
            new_node = DoublyNode(data)
        self.head = new_node
        self.tail = new_node

    # ========================= Basic Operations ==========================
    def is_empty(self):
        """
        Checks whether the doubly linked list is empty.
        
        :return: True if the list is empty, otherwise False.
        """
        return self.head is None
    
    def get_length(self):
        """
        Gets the number of nodes in the list by traversing through head or the tail.
                                    OR
        Calculates the number of nodes present in the doubly linked list.
        
        Traverses the list from both the head and tail, counting the nodes until 
        the two pointers meet.  

        :return: The length of the list OR The total count of nodes in the list.
        """
        if self.is_empty():
            return 0

        # Initialize two pointers, one from the head and one from the tail
        head_ptr = self.head
        tail_ptr = self.tail
        count = 0

        # Traverse from both ends towards the center
        while head_ptr != tail_ptr and head_ptr and tail_ptr:
            count += 1
            head_ptr = head_ptr.next
            tail_ptr = tail_ptr.next
        
        # If both pointers meet at the same node (odd number of nodes)
        if head_ptr == tail_ptr:
            count += 1

        return count

    def print_list(self):
        """
        Prints the nodes in the list from head to tail.
        """
        if self.is_empty():
            print("List is empty.")
            return

        curr = self.head
        items = []
        # Traverse through the list, collecting the values of each node
        while curr:
            items.append(str(curr.data))
            curr = curr.next
        print(" <-> ".join(items))

    def print_reverse(self):
        """
        Prints the nodes in the list from tail to head.
        """
        pass

    # ========================= Insert Operations ==========================
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

    def insert_after(self, prev_value, data):
        """
        Inserts a new node with the given data after the node with the specified value.
        
        :param prev_value: The value of the node after which to insert the new node.
        :param data: The value to insert.
        :return: True if the operation was successful, otherwise False.
        """
        pass

    def insert_before(self, next_value, data):
        """
        Inserts a node before a specified node value.
        :param next_value: The value of the node to insert before.
        :param data: The value to insert.
        :return: True if successful, False if the next node is not found.
        """
        pass

    # ========================= Deletion Operations ==========================
    def delete(self, key):
        """
        Deletes the node with the specified key.
        
        :param key: The value of the node to be deleted.
        :return: True if the operation was successful, otherwise False.
        """
        pass

    def delete_first(self):
        """
        Deletes the first node in the list.
        :return: True if deletion was successful, False if the list is empty.
        """
        pass

    def delete_last(self):
        """
        Deletes the last node in the list.
        :return: True if deletion was successful, False if the list is empty.
        """
        pass

    # ======================= Search and Edit Operations ======================
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

    # ======================= Utility Operations ======================
    def clear(self):
        """
        Clears the entire linked list.
        """
        pass

    def to_list(self):
        """
        Converts the linked list to a standard Python list.
        :return: List of values from head to tail.
        """
        pass

    def to_list_reverse(self):
        """
        Converts the linked list to a standard Python list in reverse order.
        :return: List of values from tail to head.
        """
        pass