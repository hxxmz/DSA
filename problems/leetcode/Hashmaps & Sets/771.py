# 771. Jewels and Stones

def numJewelsInStones(jewels: str, stones: str) -> int:

    # Time: O(m + n)
    # Space: O(m)

    occurences = {}

    for jewel in jewels: # O(m)
        occurences[jewel] = 0
    
    for stone in stones: # O(n)
        if stone in occurences: # O(1) avg-case lookup
            occurences[stone] += 1
    
    count = 0
    for val in occurences.values(): # O(m)
        count += val

    return count

def numJewelsInStonesTwo(jewels: str, stones: str) -> int: 

    # Time: O(m + n)
    # 

    jewel_set = set(jewels) # O(m) time and space
    
    count = 0
    for stone in stones: # O(n)
        if stone in jewel_set: # O(1) avg-case lookup
            count += 1
       
    return count

print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(numJewelsInStones(jewels = "z", stones = "ZZ"))

print(numJewelsInStonesTwo(jewels = "aA", stones = "aAAbbbb"))
print(numJewelsInStonesTwo(jewels = "z", stones = "ZZ"))
