from typing import List

# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        answer_interval = intervals[0]
        index = 1
        while index < len(intervals):
            current_interval = intervals[index]

            if current_interval[0] <= answer_interval[1]:
                if answer_interval[1] < current_interval[1]:
                    answer_interval[1] = current_interval[1]
            else:
                answer.append(answer_interval)
                answer_interval = current_interval
            
            if index == len(intervals) - 1:
                answer.append(answer_interval)

            index += 1

        return answer

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),  # Expected output: [[1, 6], [8, 10], [15, 18]]
        ([[1, 4], [4, 5]], [[1, 5]]),  # Expected output: [[1, 5]]
    ]

    print("Testing merge:")
    for i, (intervals, expected) in enumerate(test_cases):
        result = sol.merge(intervals)
        print(f"Test case {i + 1}:")
        print(f"  Output: {result} | Expected: {expected} {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    test()
