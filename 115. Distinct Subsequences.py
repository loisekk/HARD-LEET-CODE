class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        n = len(t)
        o = [0]*(n+1)
        o[0] = 1
        for i in range(len(s)):
            for j in range(n-1 , -1 , -1):
                if s[i] == t[j]:
                    o[j+1] += o[j]
        return o[n]
