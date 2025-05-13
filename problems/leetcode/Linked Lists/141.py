from typing import Optional
from linkedlist_utils import ListNode, list_to_linkedlist, create_cycle

# 141. Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # My thought process is that we will run two pointers simultaneously,
        # one pointer moves twice the speed of the second,
        # if the second pointer finds the first pointer then we say it is cycled.
        # if we hit None before pointers meet again then it is not cycled.
        # This is also called "Floyd's Tortoise and Hare Algorithm"

        if head is None or head.next is None:
            return False

        slow = head
        fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Test Function
def test():
    sol = Solution()
    
    # Test Cases
    test_cases = [
        ([3, 2, 0, -4], 1, True),   # Cycle at node with value 2
        ([1, 2], 0, True),          # Cycle at node with value 1
        ([1], -1, False),           # Single node with no cycle
        ([1, 2, 3, 4, 5], -1, False), # No cycle in a multi-node list
        ([], -1, False),            # Empty list, no cycle
        ([1, 2, 3], 2, True),       # Cycle back to the last node
    ]

    for i, (input_list, pos, expected_output) in enumerate(test_cases):
        ll_input = list_to_linkedlist(input_list)
        ll_input = create_cycle(ll_input, pos)
        result = sol.hasCycle(ll_input)
        print(f"Test case {i + 1}: {'✅' if result == expected_output else '❌'} | Output: {result} | Expected: {expected_output}")

if __name__ == "__main__":
    test()