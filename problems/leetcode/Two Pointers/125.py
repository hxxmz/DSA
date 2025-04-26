# 125. Valid Palindrome
import re

def isPalindrome(s: str) -> bool:

    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    if len(s) == 0:
       return True

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
           return False
        l += 1
        r -= 1
    
    return True

print(isPalindrome(s = "A man, a plan, a canal: Panama"))
print(isPalindrome(s = "race a car"))
print(isPalindrome(s = " "))
