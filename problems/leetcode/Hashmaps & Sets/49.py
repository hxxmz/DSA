from typing import List

# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # initially thought to use word weight as signatures and set weight to avoid collision on weights
        # better solution can also be char count tuple, instead of assigning weights, i overwite count on index
        # use those tuples as keys to group them together in a hashmap

        hashmap = {}
        for word in strs:
            char_counts = [0] * 26
            for letter in word:
                idx = ord(letter) - ord("a")
                char_counts[idx] += 1
            char_key = tuple(char_counts)
            hashmap.setdefault(char_key, []).append(word)

        return [val for val in hashmap.values()]

# Test function
def test():
    sol = Solution()

    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    for i, (strs, expected) in enumerate(test_cases):
        result = sol.groupAnagrams(strs)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()