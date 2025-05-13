from typing import Optional
from linkedlist_utils import ListNode, list_to_linkedlist, linkedlist_to_list

# 21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        elif list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        
        # make a new linked list not caring about space for the moment
        if list1.val <= list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next
        
        cll = head
        while list1 or list2:
            if not list1:
                cll.next = list2
                list2 = None

            elif not list2:
                cll.next = list1
                list1 = None

            elif list1.val <= list2.val:
                cll.next = list1
                cll = cll.next
                list1 = list1.next
            
            else:
                cll.next = list2
                cll = cll.next
                list2 = list2.next

        return head

# Test Function
def test():
    sol = Solution()
    
    # Test Cases
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),            # Standard merge case
        ([], [], []),                                          # Both lists empty
        ([1, 3, 5], [], [1, 3, 5]),                            # One list empty, other filled
        ([], [2, 4, 6], [2, 4, 6]),                            # One list empty, other filled
        ([1], [1], [1, 1]),                                    # Single element lists
        ([2, 3, 7], [1, 4, 5, 8], [1, 2, 3, 4, 5, 7, 8]),      # Uneven lengths
        ([5, 10, 15], [2, 4, 6], [2, 4, 5, 6, 10, 15]),        # Different ranges
    ]

    for i, (list1, list2, expected_output) in enumerate(test_cases):
        ll1 = list_to_linkedlist(list1)
        ll2 = list_to_linkedlist(list2)
        result = linkedlist_to_list(sol.mergeTwoLists(ll1, ll2))
        print(f"Test case {i + 1}: {'✅' if result == expected_output else '❌'} | Output: {result} | Expected: {expected_output}")

if __name__ == "__main__":
    test()