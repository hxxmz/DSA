# 344. Reverse String
from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    print(s)

reverseString(s = ["h","e","l","l","o"])
reverseString(s = ["H","a","n","n","a","h"])