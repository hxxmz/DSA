from typing import List

# 274. H-Index
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort() # sort
        citations = citations[::-1] # reverse

        i = 0
        while i < len(citations) and citations[i] >= i + 1:
            i += 1

        return i

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([3, 0, 6, 1, 5], 3),
        ([1, 3, 1], 1),
        ([100, 99, 98, 97, 96, 95, 94, 93, 92, 91], 10),
        ([0, 0, 0, 0], 0),
        ([1], 1),
        ([1, 1, 1, 1], 1),
        ([7, 7, 7, 7], 4),
        ([1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 3, 5, 5, 2, 5], 4),
    ]

    for i, (citations, expected) in enumerate(test_cases):
        result = sol.hIndex(citations)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()
