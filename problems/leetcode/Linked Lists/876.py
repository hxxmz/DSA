from typing import Optional
from linkedlist_utils import ListNode, list_to_linkedlist, linkedlist_to_list

# 876. Middle of the Linked List
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if fast.next is None:
                break
        
        if fast.next:
            return slow.next
        
        return slow
    
    def middleNodeTwo(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
       
        return slow

# Test Function
def test():
    sol = Solution()
    
    # Test Cases
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5]),             # Odd number of nodes, middle is 3
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),          # Even number of nodes, middle is 4 (2nd middle)
        ([1], [1]),                               # Single node, middle is itself
        ([1, 2], [2]),                            # Two nodes, middle is the second one
        ([10, 20, 30, 40, 50, 60, 70], [40, 50, 60, 70]), # Larger list, middle is 40
    ]

    for i, (input_list, expected_output) in enumerate(test_cases):
        ll_input = list_to_linkedlist(input_list)
        result = linkedlist_to_list(sol.middleNode(ll_input))
        print(f"Test case A{i + 1}: {'✅' if result == expected_output else '❌'} | Output: {result} | Expected: {expected_output}")
    
    for i, (input_list, expected_output) in enumerate(test_cases):
        ll_input = list_to_linkedlist(input_list)
        result = linkedlist_to_list(sol.middleNodeTwo(ll_input))
        print(f"Test case B{i + 1}: {'✅' if result == expected_output else '❌'} | Output: {result} | Expected: {expected_output}")

if __name__ == "__main__":
    test()