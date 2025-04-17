def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    l = 0
    r = m
    s = 0

    while s < len(nums2):
        if nums1[l] == 0:
            nums1[l] = nums2[s]
            l += 1
            r += 1
            s += 1
            continue

        if nums1[l] <= nums2[s]:
            l += 1
            continue

        nums1[r] = nums2[s]
        nums1[l], nums1[r] = nums1[r], nums1[l]
        r += 1
        s += 1
        l += 1
    
    print(nums1)
 

merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
merge(nums1 = [1], m = 1, nums2 = [], n = 0)
merge(nums1 = [0], m = 0, nums2 = [1], n = 1)