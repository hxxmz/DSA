# 383. Ransom Note

def canConstruct(ransomNote: str, magazine: str) -> bool:
    
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

print(canConstruct(ransomNote = "a", magazine = "b"))
print(canConstruct(ransomNote = "aa", magazine = "ab"))
print(canConstruct(ransomNote = "aa", magazine = "aab"))
print(canConstruct(ransomNote = "aab", magazine = "aaabbb"))
