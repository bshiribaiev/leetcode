"""
link to the problem:
https://leetcode.com/problems/maximum-product-of-three-numbers/description/

date: May 26, 2025

O(n)
"""

from typing import List

def maxProduct(self, nums: List[int]) -> int:
        currentMax = currentMin = maxProd = nums[0] 

        for i in range(1, len(nums)):
            tempMax = currentMax * nums[i]
            tempMin = currentMin * nums[i]

            if nums[i] > tempMax:
                currentMax = nums[i]
            else: 
                currentMax = tempMax

            if currentMax < tempMin:
                currentMax = tempMin
            
            if nums[i] < tempMin:
                currentMin = nums[i]
            else:
                currentMin = tempMin
                
            if currentMin > tempMax:
                currentMin = tempMax
            
            if maxProd < currentMax:
                maxProd = currentMax
        
        return maxProd