import re

# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean text into alphanumeric chars
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        if len(s) == 0:
            return True

        # Strict checking of mirroring indices
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

# Test function
def test():
    sol = Solution()
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("Able was I ere I saw Elba", True),
        ("No lemon, no melon", True),
    ]
    
    for i, (s, expected) in enumerate(test_cases):
        result = sol.isPalindrome(s)
        print(f"Test case {i+1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()
