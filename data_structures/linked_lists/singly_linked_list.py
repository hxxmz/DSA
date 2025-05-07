class SinglyNode:
    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value

    def __str__(self):
        return str(self.value)

class SinglyLinkedList:
    def __init__(self, data):
        new_node = SinglyNode(data)
        self.head = new_node

    def prepend(self, data):
        """
        Prepend a node to the linked list.

        Parameters
        ----------
        data : the data to prepend

        Notes
        -----
        If the linked list is empty, the new node is set as the head.
        Otherwise, the new node is prepended to the head of the linked list
        """
        new_node = SinglyNode(data)
        curr = self.head

        if not curr:
            self.head = new_node
            return

        self.head = new_node
        new_node.next = curr

    def append(self, data):
        new_node = SinglyNode(data)
        curr = self.head

        if not curr:
            self.head = new_node
            return
        
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def is_empty(self):
        return self.head is None

    def insert_after(self, prev_value, data):
        prev_node = self.find_node(prev_value)
        if prev_node:
            new_node = SinglyNode(data)
            new_node.next = prev_node.next
            prev_node.next = new_node
            return True
        else:
            print(f"Node with value '{prev_value}' not found. Cannot insert.")
            return False

    def delete(self, key):
        curr = self.head 
        if not curr:
            return 
        
        if curr.value == key:
            self.head = curr.next

        while curr.next:
            if curr.next.value == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        return

    def search(self, key):
        curr = self.head
        if curr:
            while curr:
                if curr.value == key:
                    return True
                curr = curr.next
        return False

    def find_node(self, key):
        curr = self.head
        if curr:
            while curr:
                if curr.value == key:
                    return curr
                curr = curr.next
        return None

    def get_length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def print_list(self):
        curr = self.head
        items = []
        while curr:
            items.append(curr.__str__())
            curr = curr.next
        print(" -> ".join(items))

# Linked list operations
ll = SinglyLinkedList(5)
ll.append(2)
ll.append(1)
ll.append(10)
ll.append(17)
ll.print_list()
print(ll.search(17))
print(ll.search(18))
