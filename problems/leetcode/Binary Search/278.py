from typing import List

def isBadVersion(version: int) -> bool:
    # This would be set during the test. Here, it's just a placeholder.
    # Example: If the first bad version is 4, then versions 4, 5, 6... are bad.
    return version >= Solution.first_bad_version_stub

# 278. First Bad Version
class Solution:
    first_bad_version_stub = None

    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2
            if isBadVersion(m): 
                r = m
            else:
                l = m + 1
        
        return r

# Test Function
def test():
    sol = Solution()

    test_cases = [
        (5, 4, 4),       # First bad version is 4 out of 5
        (1, 1, 1),       # Only one version and it's bad
        (10, 7, 7),      # First bad version is 7 out of 10
        (100, 50, 50),   # First bad version is 50 out of 100
        (20, 20, 20),    # The very last version is bad
        (2, 2, 2),       # Small case, only two versions, second one is bad
    ]

    for i, (n, bad_version, expected) in enumerate(test_cases):
        # Setting the mock bad version for this test
        Solution.first_bad_version_stub = bad_version

        result = sol.firstBadVersion(n)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()