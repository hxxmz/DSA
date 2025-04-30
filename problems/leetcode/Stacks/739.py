from typing import List

# 739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # initially i stacked up the temperatures, popping backwards differences,
        # then i stacked up indices and moved backwards until i realized;
        # we move forward checking the stack, if it is empty, push the day/index and move ahead.
        # if the stack is not empty, i first check if the current index temperature > stack top temperature,
        # i keep going backwards settling every day that the current index temperature is warmer from.
        # i append the index of the current temperature and move ahead.
        # all of the temperatures that didn't see a warmer day in the stack, retain their intialized 0.

        length = len(temperatures)
        answer = [0] * length
        stk = []
        day = 0
        while day < length:
            if stk:
                while stk and temperatures[day] > temperatures[stk[-1]]:
                    answer[stk[-1]] = day - stk[-1]
                    stk.pop()
            stk.append(day)
            day += 1

        return answer

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),  # regular case
        ([30, 40, 50, 60], [1, 1, 1, 0]),  # strictly increasing
        ([30, 20, 10], [0, 0, 0]),  # strictly decreasing
        ([70, 70, 70, 70], [0, 0, 0, 0]),  # no increase
        ([80, 60, 90, 100], [2, 1, 1, 0]),  # alternating pattern
        ([50], [0]),  # single element
        ([], []),  # empty list
    ]

    for i, (temps, expected) in enumerate(test_cases):
        result = sol.dailyTemperatures(temps)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()