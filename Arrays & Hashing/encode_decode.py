"""
link to the problem: 
https://neetcode.io/problems/string-encode-and-decode

date: May 24, 2025
"""

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += str(len(word)) + '#' + word
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        length = len(s)
        i = 0

        while i < length:
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            i = j + 1
            j = i + num
            res.append(s[i:j])
            i = j 
        return res