# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        for i in range(0, len(s)):
            if i+1 == len(s) or roman[s[i]] >= roman[s[i+1]]:
                result += roman[s[i]]
            else:
                result -= roman[s[i]] 
        return result

    def romanToIntTwo(self, s: str) -> int:
        roman = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        result = roman[s[len(s)-1]]
        for i in range(len(s)-2, -1, -1):
            if roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result

# Test function
def test():
    sol = Solution()
    
    test_cases = [
        ("XIV", 14),
        ("L", 50),
        ("IX", 9),
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994)
    ]

    for i, (roman, expected) in enumerate(test_cases):
        result1 = sol.romanToInt(roman)
        result2 = sol.romanToIntTwo(roman)
        print(f"Test case {i + 1}:")
        print(f"  romanToInt: {'✅' if result1 == expected else '❌'} | Output: {result1} | Expected: {expected}")
        print(f"  romanToIntTwo: {'✅' if result2 == expected else '❌'} | Output: {result2} | Expected: {expected}")

if __name__ == "__main__":
    test()