class SinglyNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
    -----------
    value : Any
        The value stored in the node.
    next : SinglyNode or None
        The reference to the next node in the list.
    """
    def __init__(self, value, next_value=None):
        """
        Initializes a SinglyNode with a value and an optional reference 
        to the next node.
        
        Parameters:
        -----------
        value : Any
            The value to store in this node.
        next_value : SinglyNode or None, optional
            The next node in the list (default is None).
        """
        self.value = value
        self.next = next_value

    def __str__(self):
        """
        Returns the string representation of the node's value.
        
        Returns:
        --------
        str
            The value of the node as a string.
        """
        return str(self.value)

class SinglyLinkedList:
    """
    A class representing a singly linked list.
    
    Attributes:
    -----------
    head : SinglyNode or None
        The head (first node) of the linked list.
    
    Methods:
    --------
    is_empty() -> bool
        Checks if the list is empty.
    get_length() -> int
        Returns the number of nodes in the list.
    print_list() -> None
        Prints all the elements in the list.
    prepend(data: Any) -> bool
        Adds a new node with the given data at the beginning of the list.
    append(data: Any) -> bool
        Adds a new node with the given data at the end of the list.
    insert_after(prev_value: Any, data: Any) -> bool
        Inserts a new node after the specified value.
    delete(key: Any) -> bool
        Deletes the first node with the specified key.
    search(key: Any) -> bool
        Searches for a node with the specified key.
    find_node(key: Any) -> SinglyNode or None
        Finds and returns the node object with the specified key.
    edit_node(key: Any, data: Any) -> bool
        Updates the value of a specified node.
    """
    # ========================== Initialization ============================
    def __init__(self, data=None):
        """
        Initializes the list with an optional single node.
        
        Parameters:
        -----------
        data : Any, optional
            The initial value for the first node (default is None).
        """
        new_node = None
        if data is not None:      
            new_node = SinglyNode(data)
        self.head = new_node

    # ========================= Basic Operations ===========================
    def is_empty(self) -> bool:
        """
        Checks if the list is empty.
        
        Returns:
        --------
        bool: True if the list is empty, otherwise False.
        """
        return self.head is None
    
    def get_length(self) -> int:
        """
        Counts and returns the number of nodes in the list.
        
        Returns:
        --------
        int: The number of nodes in the list.
        """
        curr = self.head
        count = 0
        # Traverse through the list, incrementing count for each node
        while curr:
            count += 1
            curr = curr.next
        return count

    def print_list(self) -> None:
        """
        Prints the elements of the list in order.
        """
        curr = self.head

        if not curr:  # Handle empty list
            print("List is empty.")
            return

        items = []
        while curr:
            items.append(str(curr))
            curr = curr.next
        print(" -> ".join(items))

    # ========================= Insert Operations ==========================
    def prepend(self, data) -> bool:
        """
        Adds a new node with the given data at the beginning of the list.
        
        Parameters:
        -----------
        data : Any
            The value to be added at the beginning.
        
        Returns:
        --------
        bool: True if the operation is successful, False otherwise.
        """
        if data is None:
            print("Cannot prepend None value.")
            return False
        
        new_node = SinglyNode(data)
        new_node.next = self.head
        self.head = new_node
        return True

    def append(self, data) -> bool:
        """
        Adds a new node with the given data at the end of the list.
        
        Parameters:
        -----------
        data : Any
            The value to be added at the end.
        
        Returns:
        --------
        bool: True if the operation is successful, False otherwise.
        """
        if data is None:
            print("Cannot append None value.")
            return False

        new_node = SinglyNode(data)

        # If the list is empty, new_node becomes the head
        if self.is_empty():
            self.head = new_node
            return True
        
        # Traverse to the last node
        curr = self.head
        while curr.next:
            curr = curr.next

        # Append the new node
        curr.next = new_node
        return True

    def insert_after(self, prev_value, data) -> bool:
        """
        Inserts a new node with the specified data after the given value.
        
        Parameters:
        -----------
        prev_value : Any
            The value after which the new node should be inserted.
        data : Any
            The value to be inserted.
        
        Returns:
        --------
        bool: True if the operation is successful, False otherwise.
        """
        prev_node = self.find_node(prev_value)

        if prev_node:
            new_node = SinglyNode(data)
            new_node.next = prev_node.next
            prev_node.next = new_node
            return True
        else:
            print(f"Cannot insert after node: Value '{prev_value}' not found.")
            return False

    # ========================= Deletion Operations ========================
    def delete(self, key) -> bool:
        """
        Deletes the node with the specified key.
        
        Parameters:
        -----------
        key : Any
            The value of the node to be deleted.
        
        Returns:
        --------
        bool: True if the operation is successful, False otherwise.
        """
        curr = self.head

        # If the list is empty, just return False
        if not curr:
            print("List is empty.")
            return False
        
        # If the node to delete is the head
        if curr.value == key:
            self.head = curr.next
            return True

        # Traverse to find the node to delete
        while curr.next:
            if curr.next.value == key:
                curr.next = curr.next.next
                return True
            curr = curr.next
        
        # If the key wasn't found
        print(f"Node with value '{key}' not found.")
        return False

    # ==================== Searching & Retreival Operations ================
    def search(self, key) -> bool:
        """
        Checks if a node with the specified key exists in the list.
        """
        return self.find_node(key) is not None

    def find_node(self, key):
        """
        Finds and returns the node with the specified key.
        """
        curr = self.head
        while curr:
            if curr.value == key:
                return curr
            curr = curr.next
        return None

    # ========================= Update Operations ==========================
    def edit_node(self, key, data) -> bool:
        """
        Edits the value of the specified node.
        """
        if data is None:
            print("Cannot set node value to None using edit_node.")
            return False
        
        node = self.find_node(key)
        if node:
            node.value = data
            return True
        
        print(f"Cannot edit: Node with value '{key}' not found.")
        return False
    
    # ======================== Utility Operations ==========================
    def reverse_list(self) -> None:
        """Reverses the entire linked list in place."""
        pass

    def remove_duplicates(self) -> None:
        """Removes duplicate values from the list."""
        pass

    def to_list(self) -> list:
        """Converts the linked list to a standard Python list."""
        pass

    def sort_list(self) -> None:
        """Sorts the linked list in ascending order."""
        pass

if __name__ == "__main__":
    # Linked list operations
    ll = SinglyLinkedList(5)
    ll.append(2)
    ll.append(1)
    ll.append(10)
    ll.append(17)
    ll.print_list()
    print(ll.search(17))
    print(ll.search(18))
