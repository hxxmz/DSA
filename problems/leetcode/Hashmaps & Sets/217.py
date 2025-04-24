# 217. Contains Duplicate

def containsDuplicate(nums) -> bool:
    # Time: O(n)
    # Space: O(n)
    return len(set(nums)) != len(nums)

print(containsDuplicate(nums = [1,2,3,1]))
print(containsDuplicate(nums = [1,2,3,4]))
print(containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))