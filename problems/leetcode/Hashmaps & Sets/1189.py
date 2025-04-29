# 1189. Maximum Number of Balloons
class Solution:   
    def maxNumberOfBalloons(self, text: str) -> int:

        # Time: O(n)
        # Space: O(1)

        # we could either make 'balloon' a set
        # and maintain count of each letter of 'balloon' in a hashmap.
        # we return the min(count of letters)  of count according to counts in 'balloon'.
        # OR
        # we init hashmap as 'balloon' chars, maintain count in it,
        # returning min(count of letters) the same way as before.

        counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for letter in text:
            if letter in counts:
                counts[letter] += 1

        return min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] // 2,
            counts['n']
        )

# Test function
def test():
    sol = Solution()

    test_cases = [
        ("nlaebolko", 1),
        ("loonbalxballpoon", 2),
        ("leetcode", 0),
        ("ballllllllllllooooooooooonnnnnnnnnbbbbaaaa", 5),
        ("", 0),
        ("balloonballoon", 2),
        ("baonxxolln", 1)
    ]

    for i, (text, expected) in enumerate(test_cases):
        result = sol.maxNumberOfBalloons(text)
        print(f"Test {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()