"""
link to the problem:
https://leetcode.com/problems/valid-anagram/description/

date: May 21, 2025
"""

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sdict = {}
        tdict = {}

        for l in s:
            sdict[l] = sdict.get(l, 0) + 1

        for l in t:
            tdict[l] = tdict.get(l, 0) + 1
        
        for l in t:
            if l not in sdict or tdict[l] != sdict[l]:
                return False
        
        return True