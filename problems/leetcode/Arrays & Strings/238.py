def productExceptSelf(nums):
    length = len(nums)
    answer = [0] * length

    # calculate the accumulative product from the left and right of the each index  
    prefix_products = [0] * length
    product = 1
    for i in range(length):
        prefix_products[i] = product
        product *= nums[i]
    # print(prefix_products)

    product = 1
    suffix_products = [0] * length
    for i in range(length-1, -1, -1):
        suffix_products[i] = product
        product *= nums[i]
    # print(suffix_products)

    # product of current index is the product of sub arrays left and right to it
    for i in range(length):
        answer[i] = prefix_products[i] * suffix_products[i]

    return answer

print(productExceptSelf(nums = [1,2,3,4]))
print(productExceptSelf(nums = [-1,1,0,-3,3]))
