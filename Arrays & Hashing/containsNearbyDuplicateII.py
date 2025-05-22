"""
link to the problem:
https://leetcode.com/problems/contains-duplicate-ii/description/

date: May 20, 2025
"""

from typing import List

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}

        for i in range(len(nums)):
            if nums[i] in temp:
                if abs(temp[nums[i]] - i) <= k:
                    return True
                temp[nums[i]] = i    
            else:        
                temp[nums[i]] = i
        return False