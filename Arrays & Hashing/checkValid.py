"""
link to the problem:
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/

date: May 28, 2025

O(n)
"""

from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        val_set = set(range(1, n + 1))

        for row in matrix:
            if set(row) != val_set:
                return False

        for col in zip(*matrix):
            if set(col) != val_set:
                return False
                
        return True