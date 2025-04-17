def productExceptSelf(nums):
    length = len(nums)
    answer = [0]*length
    
    prefixProduct = [0] * length
    product = 1
    for i in range(length):
        prefixProduct[i] = product
        product *= nums[i]
    
    product = 1

    print(prefixProduct)




    return answer

print(productExceptSelf(nums = [1,2,3,4]))
# print(productExceptSelf(nums = [-1,1,0,-3,3]))
