def isSubsequence(s: str, t: str) -> bool:
    ptrS = 0
    ptrT = 0
    while ptrT < len(t) and ptrS < len(s):
        if s[ptrS] == t[ptrT]:
            ptrS += 1
        ptrT += 1
    if ptrS == len(s):
        return True
    return False

print(isSubsequence(s = "axc", t = "ahbgdc"))