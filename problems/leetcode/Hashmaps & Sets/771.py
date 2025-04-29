# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # Time: O(m + n)
        # Space: O(m)

        # iterate through jewels to know what to look in stones.
        # iterate through stones, counting those jewels.
        # sum the count of those jewels.

        occurences = {}

        for jewel in jewels: # O(m)
            occurences[jewel] = 0
        
        for stone in stones: # O(n)
            if stone in occurences: # O(1) avg-case lookup
                occurences[stone] += 1
        
        count = 0
        for val in occurences.values(): # O(m)
            count += val

        return count

    def numJewelsInStonesTwo(self, jewels: str, stones: str) -> int: 

        # Time: O(m + n)
        # Space: O(1)

        # convert jewel into a set for constant lookup.
        # for every stone that is in jewel_set, count++.

        jewel_set = set(jewels) # O(m) time and space
        
        count = 0
        for stone in stones: # O(n)
            if stone in jewel_set: # O(1) avg-case lookup
                count += 1
        
        return count

# Test function
def test():
    sol = Solution()

    test_cases = [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
        ("bcd", "abcabcabc", 6),
        ("", "abc", 0),
        ("abc", "", 0),
    ]

    for i, (jewels, stones, expected) in enumerate(test_cases):
        result1 = sol.numJewelsInStones(jewels, stones)
        result2 = sol.numJewelsInStonesTwo(jewels, stones)
        correct = result1 == expected and result2 == expected
        print(f"Test case {i + 1}: {'✅' if correct else '❌'} | Output1: {result1} | Output2: {result2} | Expected: {expected}")

if __name__ == "__main__":
    test()