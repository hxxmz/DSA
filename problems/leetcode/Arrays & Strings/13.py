def romanToInt(s: str) -> int:
    result = 0
    roman = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
    for i in range(0, len(s)):
        if i+1 == len(s) or roman[s[i]] >= roman[s[i+1]]:
            result += roman[s[i]]
        else:
            result -= roman[s[i]] 
    return result

def romanToIntTwo(s: str) -> int:
    roman = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
    result = roman[s[len(s)-1]]
    for i in range(len(s)-2, -1, -1):
        if roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]
    return result

print(romanToInt('XIV'))
print(romanToInt('L'))
print(romanToInt('IX'))
print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))

print(romanToIntTwo('XIV'))
print(romanToIntTwo('L'))
print(romanToIntTwo('IX'))
print(romanToIntTwo('III'))
print(romanToIntTwo('LVIII'))
print(romanToIntTwo('MCMXCIV'))