# 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1

        if len(word1) < len(word2):
            for i in range(len(word1)):
                result += word1[i] + word2[i]
            for j in range(i+1,len(word2)):
                result += word2[j]
        else:
            for i in range(len(word2)):
                result += word1[i] + word2[i]
            for j in range(i+1,len(word1)):
                result += word1[j]
        return result

    def mergeAlternatelyTwo(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(max(len(word1), len(word2))):
            if i >= len(word1):
                result += word2[i]
            elif i >= len(word2):
                result += word1[i]
            else: 
                result += word1[i] + word2[i]
        return result

    def mergeAlternatelyThree(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return result

# Test cases
def test():
    sol = Solution()

    test_cases = [
        ("abcde", "pqrs"),  # Expected: "apbqcrsde"
        ("abc", "xyz"),  # Expected: "axbycz"
        ("abc", "xy"),  # Expected: "axbyc"
        ("abcde", ""),  # Expected: "abcde"
        ("", "pqrs"),  # Expected: "pqrs"
    ]

    for i, (word1, word2) in enumerate(test_cases):
        result1 = sol.mergeAlternately(word1, word2)
        result2 = sol.mergeAlternatelyTwo(word1, word2)
        result3 = sol.mergeAlternatelyThree(word1, word2)
        print(f"Test case {i + 1}:")
        print(f"  mergeAlternately: {result1}")
        print(f"  mergeAlternatelyTwo: {result2}")
        print(f"  mergeAlternatelyThree: {result3}")
        print('-' * 50)

if __name__ == "__main__":
    test()