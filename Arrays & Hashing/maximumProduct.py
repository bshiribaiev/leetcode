"""
link to the problem:
https://leetcode.com/problems/maximum-product-of-three-numbers/description/

date: May 26, 2025

O(nlogn)
"""

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product1 = nums[-1] * nums[-2] * nums[-3]
        product2 = nums[0] * nums[1] * nums[-1]
        if product1 > product2:
            return product1
        else:
            return product2