"""
link to the problem:
https://leetcode.com/problems/longest-consecutive-sequence/description/

date: May 29, 2025

O(n)
"""

from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
        setCons = set(nums)
        longest = 0
        
        for num in setCons:
            if num - 1 not in setCons:
                length = 1
                current = num
                while current + 1 in setCons:
                    length += 1
                    current += 1
                if length >= longest:
                    longest = length

        return longest