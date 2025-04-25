# 49. Group Anagrams
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    hashmap = {}

    for word in strs:
        
        set_weight = 0

        print(word)

    # initially thought to use word weight as signatures and set weight to avoid collision on weights
    # better solution can also be char count tuple, instead of assigning weights, i overwite count on index
    # use those tuples as keys to group them together in a hashmap

    pass

groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]) # [["bat"],["nat","tan"],["ate","eat","tea"]]
groupAnagrams(strs = [""]) # [[""]]
groupAnagrams(strs = ["a"]) # [["a"]]