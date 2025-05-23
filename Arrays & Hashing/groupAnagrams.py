"""
link to the problem:
https://leetcode.com/problems/group-anagrams/description/

date: May 23, 2025
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [['']]:
            return [['']]

        dictr = {}
        result = []
        for word in strs: 
            sortedWord = ''.join(sorted(word))
            if sortedWord in dictr:
                dictr[sortedWord].append(word)
            
            else:
                dictr[sortedWord] = [word]

        for key in dictr:
            result.append(dictr[key]) 