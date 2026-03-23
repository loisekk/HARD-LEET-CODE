class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. got the error side in 126 testcase (Time Limit Exceeded)
        # for i in range(len(s) , -1 , -1):
        #    pre = s[:i]
        #    if pre == pre[::-1]:
        #       fix =s[i:]
        #       return fix[::-1] +s

        rev = s[::-1]
        new_s = s + "#" + rev
        
        l = [0] * len(new_s)
        j = 0
        for i in range(1, len(new_s)):
            while j > 0 and new_s[i] != new_s[j]:
                j = l[j - 1]
            
            if new_s[i] == new_s[j]:
                j += 1
                l[i] = j
        
        # Characters to add
        add = rev[:len(s) - l[-1]]
        return add + s

