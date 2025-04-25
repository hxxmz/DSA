# 169. Majority Element

def majorityElement(nums) -> int:
    condition = len(nums)//2
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1
    
    answer = [0,0]
    for key,val in seen.items():
        if seen[key] > condition and seen[key] > answer[1]:
            answer[0] = key
            answer[1] = val
    
    return answer[0]

def BoyerMooreVotingAlgorithm(nums) -> int:
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

print(majorityElement(nums = [3,2,3]))
print(majorityElement(nums = [2,2,1,1,1,2,2]))

print(majorityElement(nums = [3,2,3]))
print(majorityElement(nums = [2,2,1,1,1,2,2]))
