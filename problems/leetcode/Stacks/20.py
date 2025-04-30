# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:

        # if bracket is opening kind, we push.
        # if it is closing kind, we have a dict that checks peek or pops the top element to compare if they're same
        # either works because if same we continue if difference return false right then.
        # we also make sure that we're not checking for a closing tag on an empty stack.
        # after processing all elements, we check if the stack is empty or not, returning validity as is, 
        # with empty regarding it as true.

        opening = {'(', '{', '['}
        closing = {')': '(', '}': '{', ']': '['}

        stk = []
        for char in s:
            if char in opening:
                stk.append(char)
            elif char in closing:
                if (not stk) or (closing[char] != stk[-1]):
                    return False
                stk.pop() 
        
        if stk:
            return False

        return True

# Test function
def test():
    sol = Solution()

    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),                     # Edge case: empty string
        ("((((((((", False),            # Only opening brackets
        ("))))))))", False),            # Only closing brackets
        ("(([]){})", True),             # Nested and mixed types
        ("(([]){})]", False),           # Mismatched close at end
        ("{[()()]}", True),             # Symmetric nesting
        ("{[()()]}}", False),           # Extra closing
        ("[({})](]", False),            # Wrong close at end
        ("((()(())))", True),           # Deep nesting of one type
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = sol.isValid(input_str)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()