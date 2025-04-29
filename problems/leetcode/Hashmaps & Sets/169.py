from typing import List

# 169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # count the times every candidate occurs, storing them in a hashmap.
        # iterate through the hashmap's key:val pairs;
        # that satisfy the majority element condition.

        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        answer = [0,0]
        for key,val in seen.items():
            if seen[key] > (len(nums)//2) and seen[key] > answer[1]:
                answer[0] = key
                answer[1] = val
        
        return answer[0]

    def BoyerMooreVotingAlgorithm(self, nums: List[int]) -> int:

        # we increment the count as we meet the candidate,
        # and decrement if we find someone else.
        # we pick/switch the candidate with the current index if the count is 0.
        # the counts will always cancel each other out,
        # with the candidate with the highest occurence remaining.

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([6, 6, 6, 7, 7], 6),
    ]

    print("Testing `majorityElement` (Hashmap Method):")
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.majorityElement(nums)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

    print("\nTesting `BoyerMooreVotingAlgorithm` (Optimal Method):")
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.BoyerMooreVotingAlgorithm(nums)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()