class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashsetS, hashsetT = {}, {}
        for i in range(len(s)):
            hashsetS[s[i]] = 1 + hashsetS.get(s[i], 0)
            hashsetT[t[i]] = 1 + hashsetT.get(t[i], 0)
        
        for counts in hashsetS:
            if hashsetS[counts] != hashsetT.get(counts, 0):
                return False
        return True