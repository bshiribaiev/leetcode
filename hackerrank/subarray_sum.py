def subarray_sum(nums, k):

    sumd = {0:1}
    result = 0
    csum = 0
    for num in nums:
        csum += num
        diff = csum - k
        if diff in sumd:
            result += sumd[diff]
            
        sumd[csum] = sumd.get(csum, 0) + 1
        
    return result
