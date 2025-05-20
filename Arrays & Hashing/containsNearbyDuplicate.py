"""
link to the problem:
https://leetcode.com/problems/contains-duplicate/

date: May 20, 2025
"""

def containsDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        count = 0

        for value in nums:
            temp[value] = temp.get(value, 0) + 1

        for val in temp.values():
            if val > 1:
                return True
            else:
                count += 1
                
        if count == len(nums):
            return False