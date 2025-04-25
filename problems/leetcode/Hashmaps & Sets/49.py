# 49. Group Anagrams
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    # initially thought to use word weight as signatures and set weight to avoid collision on weights
    # better solution can also be char count tuple, instead of assigning weights, i overwite count on index
    # use those tuples as keys to group them together in a hashmap

    hashmap = {}
    for word in strs:
        char_counts = [0] * 26
        for letter in word:
            idx = ord(letter) - ord("a")
            char_counts[idx] += 1
        char_key = tuple(char_counts)
        hashmap.setdefault(char_key, []).append(word)

    return [val for val in hashmap.values()]

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(strs = [""])) # [[""]]
print(groupAnagrams(strs = ["a"])) # [["a"]]