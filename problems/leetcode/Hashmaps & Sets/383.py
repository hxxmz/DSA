# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Time: O(n + m)
        # Space: O(k)

        # count all of the letters in the ransom note.
        # count all of the characters in the magazine that are in the ransom note.
        # if count of any letter of ransom note is greater than that in the magazine; cannot construct.
        # otherwise you can.

        ransomNote_count = {}
        for letter in ransomNote: # O(m)
            if letter not in ransomNote_count:
                ransomNote_count[letter] = 0
            ransomNote_count[letter] += 1
        
        magazine_count = {}
        for letter in magazine: # O(n)
            # if it's not the part of the note, its not relevant
            if letter not in ransomNote_count:
                continue
            # it exists in ransom note, we handle its count
            if letter not in magazine_count:
                magazine_count[letter] = 0
            magazine_count[letter] += 1

        # force check to make it fail, otherwise its true
        for letter in ransomNote_count.keys(): # O(m)
            if ransomNote_count[letter] > magazine_count.get(letter, 0):
                return False
        return True

    def canConstruct_opt(self, ransomNote: str, magazine: str) -> bool:

        # Time: O(n + m)
        # Space: O(k)

        # What I can also do is, ransomNote_count happens as it is.
        # We then loop over magazine and decrement everytime a letter appears in ransom.
        # After the loop, I check if sum of all values <=0, if so, then letters in magazine fulfill ransom letter requirements,
        # otherwise (sum>0) then all of the letters of the ransom note were not accounted for.

        letter_count = {}
        for letter in ransomNote:
            letter_count[letter] = letter_count.get(letter, 0) + 1
            
        for letter in magazine:
            if letter in letter_count:
                letter_count[letter] -= 1
        
        count = 0
        for val in letter_count.values():
            count += val
        
        return count <= 0

# Test function
def test():
    sol = Solution()

    test_cases = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("aab", "aaabbb", True),
        ("abc", "def", False),
        ("", "", True),
    ]

    for i, (ransomNote, magazine, expected) in enumerate(test_cases):
        result = sol.canConstruct(ransomNote, magazine)
        result_opt = sol.canConstruct_opt(ransomNote, magazine)
        correct = result == expected and result_opt == expected
        print(f"Test case {i + 1}: {'✅' if correct else '❌'} | Output: {result} | Opt: {result_opt} | Expected: {expected}")

if __name__ == "__main__":
    test()