from typing import List

# 150. Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opcode = {'+', '-', '*', '/'}
        stk = []
        for token in tokens:
            # print(stk, token, end=" ")
            if token not in opcode:
                stk.append(int(token))
                # print(stk)
                continue
            operand_two = stk.pop()
            operand_one = stk.pop()
            match token:
                case "+":
                    stk.append(operand_one + operand_two)
                case "-":
                    stk.append(operand_one - operand_two)
                case "*":
                    stk.append(operand_one * operand_two)
                case "/":
                    stk.append(int(operand_one / operand_two))
            # print(stk)
        return stk[-1]

# Test function
def test():
    sol = Solution()

    test_cases = [
        (["2", "1", "+", "3", "*"], 9),                                     # (2 + 1) * 3 = 9
        (["4", "13", "5", "/", "+"], 6),                                    # 4 + (13 / 5) = 6
        (["3", "4", "+", "2", "*", "7", "/"], 2),                           # ((3 + 4) * 2) / 7 = 2
        (["10", "6", "9", "3", "/", "-", "*"], 30),                         # 10 * (6 - (9 / 3)) = 10 * 3 = 30
        (["5"], 5),                                                         # Single number
        (["4", "2", "+"], 6),                                               # Simple addition
        (["4", "2", "-"], 2),                                               # Simple subtraction
        (["4", "2", "*"], 8),                                               # Simple multiplication
        (["4", "2", "/"], 2),                                               # Simple division
        (["4", "13", "5", "/", "+"], 6),                                    # More complex
        (["-4", "2", "/"], -2),                                             # Negative number division
        (["4", "-2", "/"], -2),                                             # Division with negative divisor
        (["4", "0", "+"], 4),                                               # Addition with zero
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),    # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 
                                                                            # = ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 
                                                                            # = ((10 * (6 / (12 * -11))) + 17) + 5 = ((10 * (6 / -132)) + 17) + 5 
                                                                            # = ((10 * 0) + 17) + 5 = (0 + 17) + 5 = 17 + 5 = 22
    ]

    for i, (tokens, expected) in enumerate(test_cases):
        result = sol.evalRPN(tokens)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()