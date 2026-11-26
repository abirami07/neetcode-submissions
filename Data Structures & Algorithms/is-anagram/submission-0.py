class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #dictionaries can track frequency, set tracks duplicates

        countingS = {}
        countingT = {}

        for i in range(len(s)):
            countingS[s[i]] = countingS.get(s[i], 0) + 1
            countingT[t[i]] = countingT.get(t[i], 0) + 1
        
        if countingS == countingT:
            return True

        return False
