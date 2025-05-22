"""
link to the problem:
https://leetcode.com/problems/two-sum/description/

date: May 22, 2025
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictn = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in dictn:
                return [i, dictn[diff]]

            dictn[nums[i]] = i