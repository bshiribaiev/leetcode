"""
link to the problem:
https://leetcode.com/problems/product-of-array-except-self/description/

date: May 27, 2025

O(n)
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1

        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        
        return res


