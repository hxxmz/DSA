def isAnagram(s: str, t: str) -> bool:

    # Time: O(n + m)
    # Space: O(k)

    seen = {}
    
    for letter in s:
        seen[letter] = seen.get(letter, 0) + 1

    for letter in t:
        if letter not in seen:
            return False
        seen[letter] -= 1
    
    for val in seen.values():
        if val != 0:
            return False

    return True

print(isAnagram(s = "anagram", t = "nagaram"))
print(isAnagram(s = "rat", t = "car"))