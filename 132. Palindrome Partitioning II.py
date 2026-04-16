class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isPalindrome(sub):
         return sub == sub[::-1]
    
        n = len(s)
        dp = [0] * n
        
        for i in range(n):
            minCuts = i
            
            for j in range(i + 1):
                if isPalindrome(s[j:i+1]):
                    if j == 0:
                        minCuts = 0
                    else:
                        minCuts = min(minCuts, dp[j-1] + 1)
            
            dp[i] = minCuts
        
        return dp[-1]
        