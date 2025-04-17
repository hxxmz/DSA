def longestCommonPrefix(strs) -> str:

    if len(strs) == 0: return ""

    resultant_prefix = strs[0] # initially, it is the shortest word
    for word in strs:
        if len(word) < len(resultant_prefix):
            resultant_prefix = word

    for word in strs:
        current_prefix = ""

        for i in range(len(resultant_prefix)):
            if word[i] == resultant_prefix[i]:
                current_prefix += word[i]
                continue
            break

        if len(current_prefix) < len(resultant_prefix):
            resultant_prefix = current_prefix
        
    return resultant_prefix

print(longestCommonPrefix(["flower","flow","flight"])) # Expected: "fl"
print(longestCommonPrefix(["dog","racecar","car"])) # Expected: ""
print(longestCommonPrefix(["hello"])) # Expected: "hello"
print(longestCommonPrefix(["apple", "apple", "apple"]))  # Expected: "apple"
print(longestCommonPrefix([]))  # Expected: "" 
