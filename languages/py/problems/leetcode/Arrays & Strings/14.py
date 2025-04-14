def longestCommonPrefix(strs) -> str:

    if len(strs) == 0: return ""

    shortest_word = strs[0]

    for word in strs:
        if len(word) < len(shortest_word):
            shortest_word = word
    
    resultant_prefix = shortest_word

    for word in strs:
        current_prefix = ""
        
        for i in range(len(shortest_word)):
            if word[i] == shortest_word[i]:
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
