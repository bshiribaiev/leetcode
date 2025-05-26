"""
link to the problem:
https://leetcode.com/problems/maximum-subarray/description/

date: May 26, 2025

Kandane's algorithm
O(n)
"""
from typing import List

def maxSubArray(self, nums: List[int]) -> int:
        c_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            if (c_sum + nums[i]) > nums[i]:
                c_sum += nums[i]
            else:
                c_sum = nums[i]

            if c_sum > max_sum:
                max_sum = c_sum
        return max_sum