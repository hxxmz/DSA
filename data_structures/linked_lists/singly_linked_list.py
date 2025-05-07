class SinglyNode:
    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value

    def __str__(self):
        return str(self.value)

class SinglyLinkedList:
    def __init__(self, data=None):
        new_node = None
        if data is not None:      
            new_node = SinglyNode(data)
        self.head = new_node

    def prepend(self, data):
        if data is None:
            print("Cannot prepend None value.")
            return False
        
        new_node = SinglyNode(data)
        new_node.next = self.head
        self.head = new_node
        return True

    def append(self, data):
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
            print(f"Cannot insert after node: Value '{prev_value}' not found.")
            return False

    def delete(self, key):
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
        while curr:
            if curr.value == key:
                return curr
            curr = curr.next
        return None

    def edit_node(self, key, data):
        if data is None:
            print("Cannot set node value to None using edit_node.")
            return False
        
        node = self.find_node(key)
        if node:
            node.value = data
            return True
        
        print(f"Cannot edit: Node with value '{key}' not found.")
        return False

    def get_length(self):
        curr = self.head
        count = 0
        # Traverse through the list, incrementing count for each node
        while curr:
            count += 1
            curr = curr.next
        return count

    def print_list(self):
        curr = self.head

        if not curr:  # Handle empty list
            print("List is empty.")
            return

        items = []
        while curr:
            items.append(str(curr))
            curr = curr.next
        print(" -> ".join(items))

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
