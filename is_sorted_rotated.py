def is_sorted_rotated(nums):
    if nums == sorted(nums):
        return True
    
    for i in range(len(nums)):
        p = nums.pop(0)
        nums.append(p)
        
        if nums == sorted(nums):
            return True
        
    return False
