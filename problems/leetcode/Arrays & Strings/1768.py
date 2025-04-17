def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
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

def mergeAlternatelyTwo(word1: str, word2: str) -> str:
    result = ""
    for i in range(max(len(word1), len(word2))):
        if i >= len(word1):
            result += word2[i]
        elif i >= len(word2):
            result += word1[i]
        else: 
            result += word1[i] + word2[i]
    return result

def mergeAlternatelyThree(word1: str, word2: str) -> str:
    result = ""
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]
    return result

print(mergeAlternately(word1 = "abcde", word2 = "pqrs"))
print(mergeAlternatelyTwo(word1 = "abcde", word2 = "pqrs"))
print(mergeAlternatelyThree(word1 = "abcde", word2 = "pqrs"))
