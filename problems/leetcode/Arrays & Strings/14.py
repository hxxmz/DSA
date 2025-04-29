from typing import List

# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0: return ""

        resultant_prefix = strs[0] # initially, it is the shortest word
        for word in strs:
            if len(word) < len(resultant_prefix):
                resultant_prefix = word

        for word in strs:
            current_prefix = ""

            for i in range(len(resultant_prefix)):
                if word[i] == resultant_prefix[i]:
                    current_prefix += word[i]
                    continue
                break

            if len(current_prefix) < len(resultant_prefix):
                resultant_prefix = current_prefix
            
        return resultant_prefix

# Test function
def test():
    sol = Solution()

    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["hello"], "hello"),
        (["apple", "apple", "apple"], "apple"),
        ([], "")
    ]

    for i, (strs, expected) in enumerate(test_cases):
        result = sol.longestCommonPrefix(strs)
        print(f"Test case {i + 1}:")
        print(f"  Output: {result} | Expected: {expected} {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    test()