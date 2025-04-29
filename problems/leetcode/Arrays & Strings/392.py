# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptrS = 0
        ptrT = 0
        while ptrT < len(t) and ptrS < len(s):
            if s[ptrS] == t[ptrT]:
                ptrS += 1
            ptrT += 1
        if ptrS == len(s):
            return True
        return False

# Test function
def test():
    sol = Solution()

    test_cases = [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("axc", "axc", True),
        ("", "ahbgdc", True),
        ("abc", "xyz", False),
    ]

    for i, (s, t, expected) in enumerate(test_cases):
        result = sol.isSubsequence(s, t)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()