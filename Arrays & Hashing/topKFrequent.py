"""
link to the problem:
https://leetcode.com/problems/top-k-frequent-elements/description/

date: May 24, 2025
"""
from typing import List

# 1st version of my solution - O(n^2)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictr = {}
        res = []

        for num in nums:
            dictr[num] = dictr.get(num, 0) + 1
        
        vals = sorted(dictr.values())

        for i in range(k):
            j = vals[-(1 + i)]

            for key, v in dictr.items():
                if v == j and key not in res:
                    res.append(key)
        return res
    
# 2nd version of my solution - O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictr = {}
        res = []
        arr = []
        for num in nums:
            dictr[num] = dictr.get(num, 0) + 1
        
        for key, v in dictr.items():
            arr.append([v, key])

        arr.sort()

        for i in range(k):
            res.append(arr.pop()[1])
        return res