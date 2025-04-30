from typing import List

# 682. Baseball Game
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for op in operations:
            match op:
                case "+":
                    # pop the top and store it and peek the next, restore stack
                    top = stk.pop()
                    peek = stk[-1]
                    stk.append(top)
                    # use top 2 vals for +
                    stk.append(top + peek)
                case "D":
                    peek = stk[-1]
                    stk.append(peek * 2)
                case "C":
                    stk.pop()
                case _:
                    stk.append(int(op))
        return sum(stk)

# Test function
def test():
    sol = Solution()

    test_cases = [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1"], 1),
        (["1", "C"], 0),
        (["1", "D", "+"], 6),
        (["10", "20", "+", "D", "C"], 60),
    ]

    for i, (operations, expected) in enumerate(test_cases):
        result = sol.calPoints(operations)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()