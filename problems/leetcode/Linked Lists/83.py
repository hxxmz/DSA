from typing import Optional
from linkedlist_utils import ListNode, list_to_linkedlist, linkedlist_to_list

# 83. Remove Duplicates from Sorted List
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        if head.next == None:
            return head
        
        saved = head
        curr = head.next
        while curr:
            if saved.val == curr.val:
                curr = curr.next
                continue
            saved.next = curr
            saved = curr
            curr = curr.next
        

def test():
    sol = Solution()

    test_cases = [
        ([1, 1, 2], [1, 2]),
        # ([1, 1, 2, 3, 3], [1, 2, 3]),
        # ([], []),
        # ([1, 1, 1, 1, 1], [1]),
        # ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ]

    for i, (input_list, expected) in enumerate(test_cases):
        ll = list_to_linkedlist(input_list)
        result_ll = sol.deleteDuplicates(ll)
        result_list = linkedlist_to_list(result_ll)
        print(f"Test case {i + 1}: {'✅' if result_list == expected else '❌'} | Output: {result_list} | Expected: {expected}")

if __name__ == "__main__":
    test()