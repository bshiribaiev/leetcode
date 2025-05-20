def intersect(nums1, nums2):
    # Write your code here
    dict1 = {}
    
    for num in nums1:
        dict1[num] = dict1.get(num, 0) + 1
        
    result = []
    
    for num in nums2:
        if num in dict1 and dict1[num] > 0:
            result.append(num)
            dict1[num] -= 1
            
    return sorted(result)
