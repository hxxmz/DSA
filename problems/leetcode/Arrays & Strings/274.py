def hIndex(citations) -> int:

    citations.sort() # sort
    citations = citations[::-1] # reverse

    i = 0
    while i < len(citations) and citations[i] >= i + 1:
        i += 1

    return i

print(hIndex(citations = [3,0,6,1,5]))
print(hIndex(citations = [1,3,1])) # 1
# edge cases
print(hIndex([100, 99, 98, 97, 96, 95, 94, 93, 92, 91])) # 10
print(hIndex([0, 0, 0, 0])) # 0

"""
Test cases:
[1] 
[1,1,1,1] 
[7,7,7,7] 
[9,9,8,8,7,7,6,6,5] 
[1,3,1] 
[0,0,0,0,0,9,9,9,7,7,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,9,9,9,7,7,1,1,1,1,1,1,1,1,1,1] 
[0,0,1,1,1,3,3,3,3,3,3,7,7,7,8,8,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6]
[1,1,1,1,2,2,2,3,3,4,4,4,3,5,5,2,5] 
[3,0,6,1,5] 
[3,0,6,1,5,3,0,6,1,5] 
[7,7,7,8,8] 
[1,1,1,1,2,2,2,3,3]
"""