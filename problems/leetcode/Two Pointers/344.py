from typing import List

# 344. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        print(s)

# Test function
def test():
    sol = Solution()
    
    test_cases = [
        (["h","e","l","l","o"], ["o","l","l","e","h"]),
        (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
        (["a"], ["a"]),
        (["x", "y"], ["y", "x"]),
        ([], []),
    ]
    
    for i, (input_list, expected) in enumerate(test_cases):
        s = input_list[:]  # copy to avoid modifying original
        sol.reverseString(s)
        print(f"Test case {i+1}: {'✅' if s == expected else '❌'} | Output: {s} | Expected: {expected}")

if __name__ == "__main__":
    test()