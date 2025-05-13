from typing import Optional
from linkedlist_utils import ListNode, list_to_linkedlist, linkedlist_to_list

# 206. Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        if head.next == None:
            return head
        
        saved = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = saved
            saved = curr
            curr = tmp
        head = saved

        return head 


# Test Function
def test():
    sol = Solution()
    
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),      # Standard reverse
        ([1], [1]),                              # Single element
        ([], []),                                # Empty list
        ([1, 2], [2, 1]),                        # Two elements
        ([1, 2, 2, 1], [1, 2, 2, 1]),            # Palindrome list
        ([5, 10, 15], [15, 10, 5]),              # Multiple of 5
        ([7, 14, 21], [21, 14, 7]),              # Multiple of 7
    ]

    for i, (input_list, expected_output) in enumerate(test_cases):
        ll_input = list_to_linkedlist(input_list)
        result = linkedlist_to_list(sol.reverseList(ll_input))
        print(f"Test case {i + 1}: {'✅' if result == expected_output else '❌'} | Output: {result} | Expected: {expected_output}")

if __name__ == "__main__":
    test()