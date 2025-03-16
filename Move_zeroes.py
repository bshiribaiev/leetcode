def count_pairs(nums, target):
    nums.sort()
    result = 0
    l, r = 0, len(nums) - 1
    
    while l < r:
        sum_n = nums[l] + nums[r]
        
        if sum_n < target:
            result += (r-l)
            l += 1
        else:
            r -= 1
        
    return result
