from typing import Optional
from linkedlist_utils import ListNode, list_to_linkedlist, linkedlist_to_list

# 2807. Insert Greatest Common Divisors in Linked List
class Solution:
    def euclidean_gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        if not head.next:
            return head
        
        curr = head
        while curr.next:
            gcd_val = self.euclidean_gcd(curr.val, curr.next.val)
            gcd_node = ListNode(gcd_val, curr.next)
            curr.next = gcd_node
            curr = gcd_node.next
        
        return head

# Test Function
def test():
    sol = Solution()
    
    test_cases = [
        ([18, 6, 10, 3], [18, 6, 6, 2, 10, 1, 3]),   # GCD of 18,6 -> 6, 6,10 -> 2, 10,3 -> 1
        ([7], [7]),                                  # Single element, no insertion
        ([18, 27, 45], [18, 9, 27, 9, 45]),          # GCD of 18,27 -> 9, 27,45 -> 9
        ([12, 15, 25], [12, 3, 15, 5, 25]),          # GCD of 12,15 -> 3, 15,25 -> 5
        ([7, 14, 28], [7, 7, 14, 14, 28]),           # GCD of 7,14 -> 7, 14,28 -> 14
        ([4], [4]),                                  # Single element, no insertion
        ([], []),                                    # Empty list, nothing to insert
    ]

    for i, (input_list, expected_output) in enumerate(test_cases):
        ll_input = list_to_linkedlist(input_list)
        result = linkedlist_to_list(sol.insertGreatestCommonDivisors(ll_input))
        print(f"Test case {i + 1}: {'✅' if result == expected_output else '❌'} | Output: {result} | Expected: {expected_output}")

if __name__ == "__main__":
    test()