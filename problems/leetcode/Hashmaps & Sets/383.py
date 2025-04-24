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

def canConstruct_opt(ransomNote: str, magazine: str) -> bool:
    """
    What I can also do is, ransomNote_count happens as it is.
    We then loop over magazine and decrement everytime a letter appears in ransom.
    After the loop, I check if sum of all values <=0, if so, then letters in magazine fulfill ransom letter requirements,
    otherwise (sum>0) then all of the letters of the ransom note were not accounted for.
    """
    ransomNote_count = {}
    for letter in ransomNote:
        ransomNote_count[letter] = ransomNote_count.get(letter, 0) + 1
        
    for letter in magazine:
        if letter in ransomNote_count:
            ransomNote_count[letter] -= 1
    
    count = 0
    for val in ransomNote_count.values():
        count += val
    
    return count <= 0

print(canConstruct(ransomNote = "a", magazine = "b"))
print(canConstruct(ransomNote = "aa", magazine = "ab"))
print(canConstruct(ransomNote = "aa", magazine = "aab"))
print(canConstruct(ransomNote = "aab", magazine = "aaabbb"))

print(canConstruct_opt(ransomNote = "a", magazine = "b"))
print(canConstruct_opt(ransomNote = "aa", magazine = "ab"))
print(canConstruct_opt(ransomNote = "aa", magazine = "aab"))
print(canConstruct_opt(ransomNote = "aab", magazine = "aaabbb"))
