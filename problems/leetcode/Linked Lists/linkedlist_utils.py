from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

def list_to_linkedlist(elements: List[int]) -> Optional[ListNode]:
    """Converts a list of integers into a linked list."""
    if not elements:
        return None

    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    """Converts a linked list back into a list of integers."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next

    return result

def create_cycle(head: ListNode, pos: int) -> ListNode:
    if pos == -1:
        return head
    
    cycle_node = None
    current = head
    index = 0

    while current.next:
        if index == pos:
            cycle_node = current
        current = current.next
        index += 1
    
    # This fixes the edge case where the cycle is supposed to connect to the last node
    if index == pos:
        cycle_node = current
        
    current.next = cycle_node
    return head