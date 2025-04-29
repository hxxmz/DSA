# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Time: O(n + m)
        # Space: O(k)

        # we iterate through the first string, counting the letters into the hashmap.
        # we do the same for the second string.
        # for first mis-match, we return false, otherwise carry on until we're done with second string.
        # we check if all the hashmap values are 0,
        # if any isn't, we return false as all letters weren't cancelled.

        seen = {}
        
        for letter in s:
            seen[letter] = seen.get(letter, 0) + 1

        for letter in t:
            if letter not in seen:
                return False
            seen[letter] -= 1
        
        for val in seen.values():
            if val != 0:
                return False

        return True

# Test function
def test():
    sol = Solution()

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "ba", True),
    ]

    for i, (s, t, expected) in enumerate(test_cases):
        result = sol.isAnagram(s, t)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()