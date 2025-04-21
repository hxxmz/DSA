def subarraySum(nums, k: int) -> int:
    length = len(nums)
    
    prefix_sum = [0] * length
    summ = 0
    for i in range(length):
        summ += nums[i]
        prefix_sum[i] = summ

    print(prefix_sum)

    answer = 0


    return answer
    

print(subarraySum(nums = [1,1,1], k = 2))
print(subarraySum(nums = [1,2,3], k = 3))